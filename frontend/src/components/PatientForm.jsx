import { useState, useEffect } from "react";
import api from "../services/api";

function PatientForm({
    refresh,
    editingPatient,
    setEditingPatient,
}) {

    const emptyForm = {
        full_name: "",
        dob: "",
        email: "",
        glucose: "",
        haemoglobin: "",
        cholesterol: ""
    };

    const [formData, setFormData] = useState(emptyForm);

    useEffect(() => {

        if (editingPatient) {

            setFormData({
                full_name: editingPatient.full_name || "",
                dob: editingPatient.dob || "",
                email: editingPatient.email || "",
                glucose: editingPatient.glucose || "",
                haemoglobin: editingPatient.haemoglobin || "",
                cholesterol: editingPatient.cholesterol || ""
            });

        }
        else {

            setFormData(emptyForm);

        }

    }, [editingPatient]);

    const handleChange = (e) => {

        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });

    };

    const submitForm = async () => {

        try {

            const payload = {
                ...formData,
                glucose: parseFloat(formData.glucose),
                haemoglobin: parseFloat(formData.haemoglobin),
                cholesterol: parseFloat(formData.cholesterol)
            };

            if (editingPatient) {

                await api.put(
                    `/patients/${editingPatient.id}`,
                    payload
                );

                alert("Patient updated successfully!");

                setEditingPatient(null);

            }
            else {

                await api.post(
                    "/patients/",
                    payload
                );

                alert("Patient added successfully!");

            }

            setFormData(emptyForm);

            refresh();

        }
        catch (error) {

            console.error(error);

            alert(
                error.response?.data?.detail ||
                "Failed to save patient."
            );

        }

    };

    const cancelEdit = () => {

        setEditingPatient(null);

        setFormData(emptyForm);

    };

    return (

    <div className="card shadow-sm border-0 mb-4">

        <div className="card-body">

            <h4 className="mb-4">

                {editingPatient
                    ? "Update Patient"
                    : "Add Patient"}

            </h4>

            <div className="row">

                <div className="col-md-4 mb-3">

                    <input
                        className="form-control"
                        name="full_name"
                        placeholder="Full Name"
                        value={formData.full_name}
                        onChange={handleChange}
                    />

                </div>

                <div className="col-md-4 mb-3">

                    <input
                        className="form-control"
                        type="date"
                        name="dob"
                        value={formData.dob}
                        onChange={handleChange}
                    />

                </div>

                <div className="col-md-4 mb-3">

                    <input
                        className="form-control"
                        type="email"
                        name="email"
                        placeholder="Email"
                        value={formData.email}
                        onChange={handleChange}
                    />

                </div>

            </div>

            <div className="row">

                <div className="col-md-4 mb-3">

                    <input
                        className="form-control"
                        type="number"
                        step="0.01"
                        name="glucose"
                        placeholder="Glucose"
                        value={formData.glucose}
                        onChange={handleChange}
                    />

                </div>

                <div className="col-md-4 mb-3">

                    <input
                        className="form-control"
                        type="number"
                        step="0.01"
                        name="haemoglobin"
                        placeholder="Haemoglobin"
                        value={formData.haemoglobin}
                        onChange={handleChange}
                    />

                </div>

                <div className="col-md-4 mb-3">

                    <input
                        className="form-control"
                        type="number"
                        step="0.01"
                        name="cholesterol"
                        placeholder="Cholesterol"
                        value={formData.cholesterol}
                        onChange={handleChange}
                    />

                </div>

            </div>

            <div>

                <button
                    className={`btn ${
                        editingPatient
                            ? "btn-warning"
                            : "btn-primary"
                    } me-2`}
                    onClick={submitForm}
                >

                    {editingPatient
                        ? "Update Patient"
                        : "Save Patient"}

                </button>

                {editingPatient && (

                    <button
                        className="btn btn-secondary"
                        onClick={cancelEdit}
                    >

                        Cancel

                    </button>

                )}

            </div>

        </div>

    </div>

);
}
export default PatientForm;