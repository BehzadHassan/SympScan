import React, { useState } from 'react';
import './DiseasePredictor.css';
import DoctorReport from './DoctorReport';

function DiseasePredictor() {
    const [name, setName] = useState('');
    const [age, setAge] = useState('');
    const [gender, setGender] = useState('');
    const [symptom, setSymptom] = useState('');
    const [symptomsList, setSymptomsList] = useState([]);
    const [response, setResponse] = useState(null);

    const symptomsOptions = ['anxiety and nervousness', 'depression', 'shortness of breath', 'depressive or psychotic symptoms', 'sharp chest pain', 'dizziness', 'insomnia', 'abnormal involuntary movements', 'chest tightness', 'palpitations', 'irregular heartbeat', 'breathing fast', 'hoarse voice', 'sore throat', 'difficulty speaking', 'cough', 'nasal congestion', 'throat swelling', 'diminished hearing', 'difficulty in swallowing', 'skin swelling', 'retention of urine', 'leg pain', 'hip pain', 'suprapubic pain', 'blood in stool', 'lack of growth', 'symptoms of the scrotum and testes', 'swelling of scrotum', 'pain in testicles', 'pus draining from ear', 'jaundice', 'white discharge from eye', 'irritable infant', 'abusing alcohol', 'fainting', 'hostile behavior', 'drug abuse', 'sharp abdominal pain', 'feeling ill', 'vomiting', 'headache', 'nausea', 'diarrhea', 'vaginal itching', 'painful urination', 'involuntary urination', 'pain during intercourse', 'frequent urination', 'lower abdominal pain', 'vaginal discharge', 'blood in urine', 'hot flashes', 'intermenstrual bleeding', 'hand or finger pain', 'wrist pain', 'hand or finger swelling', 'arm pain', 'wrist swelling', 'arm stiffness or tightness', 'arm swelling', 'hand or finger stiffness or tightness', 'lip swelling', 'toothache', 'abnormal appearing skin', 'skin lesion', 'acne or pimples', 'facial pain', 'mouth ulcer', 'skin growth', 'diminished vision', 'double vision', 'symptoms of eye', 'pain in eye', 'abnormal movement of eyelid', 'foreign body sensation in eye', 'irregular appearing scalp', 'back pain', 'neck pain', 'low back pain', 'pain of the anus', 'pain during pregnancy', 'pelvic pain', 'impotence', 'vomiting blood', 'regurgitation', 'burning abdominal pain', 'restlessness', 'wheezing', 'peripheral edema', 'neck mass', 'ear pain', 'jaw swelling', 'mouth dryness', 'neck swelling', 'knee pain', 'foot or toe pain', 'ankle pain', 'bones are painful', 'elbow pain', 'knee swelling', 'skin moles', 'weight gain', 'problems with movement', 'knee stiffness or tightness', 'leg swelling', 'foot or toe swelling', 'heartburn', 'infant feeding problem', 'vaginal pain', 'vaginal redness', 'weakness', 'decreased heart rate', 'increased heart rate', 'ringing in ear', 'plugged feeling in ear', 'itchy ear(s)', 'frontal headache', 'fluid in ear', 'spots or clouds in vision', 'eye redness', 'lacrimation', 'itchiness of eye', 'blindness', 'eye burns or stings', 'decreased appetite', 'excessive anger', 'loss of sensation', 'focal weakness', 'symptoms of the face', 'disturbance of memory', 'paresthesia', 'side pain', 'fever', 'shoulder pain', 'shoulder stiffness or tightness', 'ache all over', 'lower body pain', 'problems during pregnancy', 'spotting or bleeding during pregnancy', 'cramps and spasms', 'upper abdominal pain', 'stomach bloating', 'changes in stool appearance', 'unusual color or odor to urine', 'kidney mass', 'symptoms of prostate', 'difficulty breathing', 'rib pain', 'joint pain', 'hand or finger lump or mass', 'chills', 'groin pain', 'fatigue', 'regurgitation.1', 'symptoms of the kidneys', 'melena', 'coughing up sputum', 'seizures', 'delusions or hallucinations', 'excessive urination at night', 'bleeding from eye', 'rectal bleeding', 'constipation', 'temper problems', 'coryza', 'hemoptysis', 'allergic reaction', 'congestion in chest', 'sleepiness', 'apnea', 'abnormal breathing sounds', 'blood clots during menstrual periods', 'pulling at ears', 'gum pain', 'redness in ear', 'fluid retention', 'flu-like syndrome', 'sinus congestion', 'painful sinuses', 'fears and phobias', 'recent pregnancy', 'uterine contractions', 'burning chest pain', 'back cramps or spasms', 'back mass or lump', 'nosebleed', 'long menstrual periods', 'heavy menstrual flow', 'unpredictable menstruation', 'painful menstruation', 'infertility', 'frequent menstruation', 'sweating', 'mass on eyelid', 'swollen eye', 'eyelid swelling', 'eyelid lesion or rash', 'symptoms of bladder', 'irregular appearing nails', 'itching of skin', 'hurts to breath', 'skin dryness, peeling, scaliness, or roughness', 'skin irritation', 'itchy scalp', 'warts', 'skin rash', 'mass or swelling around the anus', 'ankle swelling', 'elbow swelling', 'bleeding from ear', 'hand or finger weakness', 'low self-esteem', 'itching of the anus', 'swollen or red tonsils', 'hip stiffness or tightness', 'mouth pain', 'arm weakness', 'obsessions and compulsions', 'antisocial behavior', 'sneezing', 'leg weakness', 'hysterical behavior', 'arm lump or mass', 'bleeding gums', 'pain in gums', 'diaper rash', 'hesitancy', 'back stiffness or tightness', 'low urine output'];
    
    const [filteredSymptoms, setFilteredSymptoms] = useState(symptomsOptions);
    const [showDropdown, setShowDropdown] = useState(false);

    const handleAddSymptom = () => {
        if (symptom.trim() && symptomsOptions.includes(symptom.trim())) {
            setSymptomsList((prev) => [...prev, symptom.trim()]);
            setSymptom('');
            setFilteredSymptoms(symptomsOptions);
        }
    };

    const handleSubmit = async () => {
        console.log('Sending symptoms:', JSON.stringify(symptomsList));

        try {
            const response = await fetch('http://localhost:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    name,
                    age,
                    gender,
                    symptomsList,
                }),
            });

            const rawText = await response.text();
            const cleanedResponse = rawText.replace(/NaN/g, 'null');

            try {
                const data = JSON.parse(cleanedResponse);
                setResponse(data);
            } catch (err) {
                console.error('Error parsing JSON:', err);
                setResponse({ error: 'Invalid JSON response from server' });
            }
        } catch (err) {
            console.error('Error:', err);
            setResponse({ error: 'Request failed' });
        }
    };

    const handleRemoveSymptom = (index) => {
        setSymptomsList((prev) => prev.filter((_, i) => i !== index));
    };

    const handleClearAll = () => {
        setName('');
        setAge('');
        setGender('');
        setSymptom('');
        setSymptomsList([]);
        setResponse(null);
    };

    return (
        <div className='container'>
            <div className="logo">
                <img src="./SympScan.png" alt="" />
                <h1>Symp<span>Scan</span></h1>
            </div>

            <div className="personal-info">
                <input
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    placeholder="Enter your name"
                />
                <input
                    type="number"
                    value={age}
                    onChange={(e) => setAge(e.target.value)}
                    placeholder="Enter your age"
                />
                <select value={gender} onChange={(e) => setGender(e.target.value)}>
                    <option value="">Select gender</option>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                    <option value="other">Other</option>
                </select>
            </div>

            <div className='input-div autocomplete-container'>
                <input
                    type="text"
                    value={symptom}
                    onChange={(e) => {
                        const val = e.target.value;
                        setSymptom(val);
                        const filtered = symptomsOptions.filter(s =>
                            s.toLowerCase().includes(val.toLowerCase())
                        );
                        setFilteredSymptoms(filtered);
                        setShowDropdown(true);
                    }}
                    onFocus={() => setShowDropdown(true)}
                    onBlur={() => {
                        setTimeout(() => {
                            setShowDropdown(false);
                        }, 200);
                    }}
                    placeholder="Enter a symptom"
                />

                <button className='symptom-add' onClick={handleAddSymptom}>Add Symptom</button>

                {showDropdown && (
                    <ul className="dropdown-list">
                        {filteredSymptoms.length === 0 ? (
                            <li className="no-option">No symptom found</li>
                        ) : (
                            filteredSymptoms.map((item, i) => (
                                <li key={i} onClick={() => {
                                    setSymptom(item);
                                    setShowDropdown(false);
                                }}>
                                    {item}
                                </li>
                            ))
                        )}
                    </ul>
                )}
            </div>

            <ul className='symptom-list'>
                {symptomsList.map((symptom, index) => (
                    <li key={index}>
                        {symptom}{' '}
                        <button className='del-btn' onClick={() => handleRemoveSymptom(index)}>Remove</button>
                    </li>
                ))}
            </ul>

            <button className='submit-btn' onClick={handleSubmit} disabled={symptomsList.length === 0 || name === '' || age === '' || gender === ''}>
                Submit
            </button>

            <button className='clear-btn' onClick={handleClearAll}>
                Clear All
            </button>

            {response && (
                <div>
                    <DoctorReport
                        name={name}
                        age={age}
                        gender={gender}
                        response={response}
                    />

                </div>
            )}
        </div>
    );
}

export default DiseasePredictor;
