import { useEffect, useState } from "react";

import api from "../services/api";

import PatientForm from "../components/PatientForm";
import PatientTable from "../components/PatientTable";
import DashboardCards from "../components/DashboardCards";

import { CSVLink } from "react-csv";

function Dashboard() {

  const [patients, setPatients] = useState([]);

  const [analytics, setAnalytics] = useState({
    total_patients: 0,
    high_risk: 0,
    moderate_risk: 0,
    low_risk: 0,
    average_health_score: 0,
  });

  const [search, setSearch] = useState("");

  const [editingPatient, setEditingPatient] = useState(null);
  const loadPatients = async () => {
    try {

      const response = await api.get("/patients");

      setPatients(response.data);

    } catch (error) {

      console.error(
        "Error loading patients:",
        error
      );

    }
  };

  const loadAnalytics = async () => {
    try {

      const response = await api.get(
        "/patients/analytics"
      );

      setAnalytics(response.data);

    } catch (error) {

      console.error(
        "Error loading analytics:",
        error
      );

    }
  };

  const refreshDashboard = () => {

    loadPatients();

    loadAnalytics();

  };

  useEffect(() => {

    refreshDashboard();

  }, []);

  const filteredPatients = patients.filter(
    (patient) =>
      patient.full_name
        .toLowerCase()
        .includes(search.toLowerCase())
  );

  return (
    <div className="container-fluid bg-light min-vh-100 py-4 px-4">

      <div className="mb-4">

    <h1 className="fw-bold text-primary">

        MIRA Health Intelligence Predictor

    </h1>

    <p className="text-muted fs-5">

        AI-Powered Healthcare Risk Assessment Platform

    </p>

</div>

      <DashboardCards
        total={analytics.total_patients}
        high={analytics.high_risk}
        moderate={analytics.moderate_risk}
        low={analytics.low_risk}
        averageScore={
          analytics.average_health_score
        }
      />

      <div className="d-flex justify-content-between align-items-center mb-3">

        <input
          type="text"
          className="form-control w-50"
          placeholder="Search Patient"
          value={search}
          onChange={(e) =>
            setSearch(e.target.value)
          }
        />

        <CSVLink
          data={patients}
          filename={"patients.csv"}
          className="btn btn-success"
        >
          Export CSV
        </CSVLink>

      </div>

      <PatientForm
    refresh={refreshDashboard}
    editingPatient={editingPatient}
    setEditingPatient={setEditingPatient}
/>

      <PatientTable
  patients={filteredPatients}
  refresh={refreshDashboard}
  setEditingPatient={setEditingPatient}
/>

    </div>
  );
}

export default Dashboard;