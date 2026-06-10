import api from "../services/api";

function PatientTable({
  patients,
  refresh,
  setEditingPatient,
})  {

  const handleDelete = async (
    patientId
  ) => {

    const confirmDelete =
      window.confirm(
        "Are you sure you want to delete this patient?"
      );

    if (!confirmDelete) {
      return;
    }

    try {

      await api.delete(
        `/patients/${patientId}`
      );

      refresh();

    } catch (error) {

      console.error(
        "Error deleting patient:",
        error
      );

      alert(
        "Failed to delete patient."
      );

    }
  };

  return (

    <div className="card shadow">

      <div className="card-body">

        <h4 className="mb-3">

          Patient Records

        </h4>

        <div className="table-responsive">

          <table className="table table-striped table-hover">

            <thead className="table-dark">

              <tr>

                <th>Name</th>

                <th>Email</th>

                <th>Glucose</th>

                <th>Hb</th>

                <th>Cholesterol</th>

                <th>Score</th>

                <th>Risk</th>

                <th>Remarks</th>

                <th>Actions</th>

              </tr>

            </thead>

            <tbody>

              {patients.length === 0 ? (

                <tr>

                  <td
                    colSpan="9"
                    className="text-center"
                  >

                    No patients found.

                  </td>

                </tr>

              ) : (

                patients.map(
                  (patient) => (

                    <tr
                      key={patient.id}
                    >

                      <td>

                        {
                          patient.full_name
                        }

                      </td>

                      <td>

                        {
                          patient.email
                        }

                      </td>

                      <td>

                        {
                          patient.glucose
                        }

                      </td>

                      <td>

                        {
                          patient.haemoglobin
                        }

                      </td>

                      <td>

                        {
                          patient.cholesterol
                        }

                      </td>

                      <td>

                        {
                          patient.health_score
                        }

                      </td>

                      <td>

                        {patient.risk_level ===
                          "High Risk" && (

                          <span className="badge bg-danger">

                            High Risk

                          </span>

                        )}

                        {patient.risk_level ===
                          "Moderate Risk" && (

                          <span className="badge bg-warning text-dark">

                            Moderate Risk

                          </span>

                        )}

                        {patient.risk_level ===
                          "Low Risk" && (

                          <span className="badge bg-success">

                            Low Risk

                          </span>

                        )}

                      </td>

                      <td>

                        {
                          patient.remarks
                        }

                      </td>

                      <td>

                       <button
  className="btn btn-sm btn-warning me-2"
  onClick={() =>
    setEditingPatient(patient)
  }
>
  Edit
</button>

<button
  className="btn btn-sm btn-danger"
  onClick={() =>
    handleDelete(patient.id)
  }
>
  Delete
</button>

                      </td>

                    </tr>

                  )
                )

              )}

            </tbody>

          </table>

        </div>

      </div>

    </div>

  );

}

export default PatientTable;