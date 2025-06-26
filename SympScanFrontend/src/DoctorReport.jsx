import React from 'react';
import './DoctorReport.css';
import 'jspdf-autotable';

function DoctorReport({ name, age, gender, response }) {
    if (!response) {
        return <p>No data available for the report.</p>;
    }

    const { description, disease, medications, precautions, symptoms, diets, workout } = response.result;
    const currentDate = new Date().toLocaleDateString();

    return (
        <div className="report-container">
            <div className="report-header">
                <h2>Doctor's Report</h2>
                <p className="report-date">{currentDate}</p>
            </div>
            <div className="report-body">
                <div className="patient-info">
                    <p><strong>Name:</strong> {name}</p>
                    <p><strong>Age:</strong> {age}</p>
                    <p><strong>Gender:</strong> {gender}</p>
                </div>
                <hr />
                <div className="diagnosis-section">
                    <h3>Diagnosis</h3>
                    <p><strong>Disease:</strong> {disease}</p>
                    <p><strong>Description:</strong> {description.join(' ')}</p>
                </div>
                <hr />
                <div className="symptoms-section">
                    <h3>Symptoms</h3>
                    <ul>
                        {symptoms.map((symptom, index) => (
                            <li key={index}>{symptom.replace('_', ' ')}</li>
                        ))}
                    </ul>
                </div>
                <hr />
                <div className="diet-section">
                    <h3>Recommended Diet</h3>
                    <ul>
                        {diets.map((diet, index) => (
                            <li key={index}>{diet}</li>
                        ))}
                    </ul>
                </div>
                <hr />
                <div className="medications-section">
                    <h3>Medications</h3>
                    <ul>
                        {medications.map((medication, index) => (
                            <li key={index}>{medication}</li>
                        ))}
                    </ul>
                </div>
                <hr />
                <div className="precautions-section">
                    <h3>Precautions</h3>
                    <ul>
                        {precautions.map((precaution, index) => (
                            <li key={index}>{precaution}</li>
                        ))}
                    </ul>
                </div>
                <hr />
                <div className="workout-section">
                    <h3>Recommended Workout</h3>
                    <ul>
                        {workout.map((workoutItem, index) => (
                            <li key={index}>{workoutItem}</li>
                        ))}
                    </ul>
                </div>
            </div>
        </div>
    );
}

export default DoctorReport;
