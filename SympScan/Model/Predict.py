import ast
import numpy as np
import pandas as pd
import pickle

symptoms_dict = {
 'abnormal appearing skin': 64,
 'abnormal breathing sounds': 171,
 'abnormal involuntary movements': 7,
 'abnormal movement of eyelid': 74,
 'abusing alcohol': 34,
 'ache all over': 136,
 'acne or pimples': 66,
 'allergic reaction': 167,
 'ankle pain': 97,
 'ankle swelling': 208,
 'antisocial behavior': 219,
 'anxiety and nervousness': 0,
 'apnea': 170,
 'arm lump or mass': 223,
 'arm pain': 57,
 'arm stiffness or tightness': 59,
 'arm swelling': 60,
 'arm weakness': 217,
 'back cramps or spasms': 184,
 'back mass or lump': 185,
 'back pain': 77,
 'back stiffness or tightness': 228,
 'bleeding from ear': 210,
 'bleeding from eye': 161,
 'bleeding gums': 224,
 'blindness': 123,
 'blood clots during menstrual periods': 172,
 'blood in stool': 25,
 'blood in urine': 51,
 'bones are painful': 98,
 'breathing fast': 11,
 'burning abdominal pain': 86,
 'burning chest pain': 183,
 'changes in stool appearance': 143,
 'chest tightness': 8,
 'chills': 151,
 'congestion in chest': 168,
 'constipation': 163,
 'coryza': 165,
 'cough': 15,
 'coughing up sputum': 157,
 'cramps and spasms': 140,
 'decreased appetite': 125,
 'decreased heart rate': 112,
 'delusions or hallucinations': 159,
 'depression': 1,
 'depressive or psychotic symptoms': 3,
 'diaper rash': 226,
 'diarrhea': 43,
 'difficulty breathing': 147,
 'difficulty in swallowing': 19,
 'difficulty speaking': 14,
 'diminished hearing': 18,
 'diminished vision': 70,
 'disturbance of memory': 130,
 'dizziness': 5,
 'double vision': 71,
 'drug abuse': 37,
 'ear pain': 91,
 'elbow pain': 99,
 'elbow swelling': 209,
 'excessive anger': 126,
 'excessive urination at night': 160,
 'eye burns or stings': 124,
 'eye redness': 120,
 'eyelid lesion or rash': 197,
 'eyelid swelling': 196,
 'facial pain': 67,
 'fainting': 35,
 'fatigue': 153,
 'fears and phobias': 180,
 'feeling ill': 39,
 'fever': 133,
 'flu-like syndrome': 177,
 'fluid in ear': 118,
 'fluid retention': 176,
 'focal weakness': 128,
 'foot or toe pain': 96,
 'foot or toe swelling': 106,
 'foreign body sensation in eye': 75,
 'frequent menstruation': 192,
 'frequent urination': 48,
 'frontal headache': 117,
 'groin pain': 152,
 'gum pain': 174,
 'hand or finger lump or mass': 150,
 'hand or finger pain': 54,
 'hand or finger stiffness or tightness': 61,
 'hand or finger swelling': 56,
 'hand or finger weakness': 211,
 'headache': 41,
 'heartburn': 107,
 'heavy menstrual flow': 188,
 'hemoptysis': 166,
 'hesitancy': 227,
 'hip pain': 23,
 'hip stiffness or tightness': 215,
 'hoarse voice': 12,
 'hostile behavior': 36,
 'hot flashes': 52,
 'hurts to breath': 201,
 'hysterical behavior': 222,
 'impotence': 83,
 'increased heart rate': 113,
 'infant feeding problem': 108,
 'infertility': 191,
 'insomnia': 6,
 'intermenstrual bleeding': 53,
 'involuntary urination': 46,
 'irregular appearing nails': 199,
 'irregular appearing scalp': 76,
 'irregular heartbeat': 10,
 'irritable infant': 33,
 'itchiness of eye': 122,
 'itching of skin': 200,
 'itching of the anus': 213,
 'itchy ear(s)': 116,
 'itchy scalp': 204,
 'jaundice': 31,
 'jaw swelling': 92,
 'joint pain': 149,
 'kidney mass': 145,
 'knee pain': 95,
 'knee stiffness or tightness': 104,
 'knee swelling': 100,
 'lack of growth': 26,
 'lacrimation': 121,
 'leg pain': 22,
 'leg swelling': 105,
 'leg weakness': 221,
 'lip swelling': 62,
 'long menstrual periods': 187,
 'loss of sensation': 127,
 'low back pain': 79,
 'low self-esteem': 212,
 'low urine output': 229,
 'lower abdominal pain': 49,
 'lower body pain': 137,
 'mass on eyelid': 194,
 'mass or swelling around the anus': 207,
 'melena': 156,
 'mouth dryness': 93,
 'mouth pain': 216,
 'mouth ulcer': 68,
 'nasal congestion': 16,
 'nausea': 42,
 'neck mass': 90,
 'neck pain': 78,
 'neck swelling': 94,
 'nosebleed': 186,
 'obsessions and compulsions': 218,
 'pain during intercourse': 47,
 'pain during pregnancy': 81,
 'pain in eye': 73,
 'pain in gums': 225,
 'pain in testicles': 29,
 'pain of the anus': 80,
 'painful menstruation': 190,
 'painful sinuses': 179,
 'painful urination': 45,
 'palpitations': 9,
 'paresthesia': 131,
 'pelvic pain': 82,
 'peripheral edema': 89,
 'plugged feeling in ear': 115,
 'problems during pregnancy': 138,
 'problems with movement': 103,
 'pulling at ears': 173,
 'pus draining from ear': 30,
 'recent pregnancy': 181,
 'rectal bleeding': 162,
 'redness in ear': 175,
 'regurgitation': 85,
 'regurgitation.1': 154,
 'restlessness': 87,
 'retention of urine': 21,
 'rib pain': 148,
 'ringing in ear': 114,
 'seizures': 158,
 'sharp abdominal pain': 38,
 'sharp chest pain': 4,
 'shortness of breath': 2,
 'shoulder pain': 134,
 'shoulder stiffness or tightness': 135,
 'side pain': 132,
 'sinus congestion': 178,
 'skin dryness, peeling, scaliness, or roughness': 202,
 'skin growth': 69,
 'skin irritation': 203,
 'skin lesion': 65,
 'skin moles': 101,
 'skin rash': 206,
 'skin swelling': 20,
 'sleepiness': 169,
 'sneezing': 220,
 'sore throat': 13,
 'spots or clouds in vision': 119,
 'spotting or bleeding during pregnancy': 139,
 'stomach bloating': 142,
 'suprapubic pain': 24,
 'sweating': 193,
 'swelling of scrotum': 28,
 'swollen eye': 195,
 'swollen or red tonsils': 214,
 'symptoms of bladder': 198,
 'symptoms of eye': 72,
 'symptoms of prostate': 146,
 'symptoms of the face': 129,
 'symptoms of the kidneys': 155,
 'symptoms of the scrotum and testes': 27,
 'temper problems': 164,
 'throat swelling': 17,
 'toothache': 63,
 'unpredictable menstruation': 189,
 'unusual color or odor to urine': 144,
 'upper abdominal pain': 141,
 'uterine contractions': 182,
 'vaginal discharge': 50,
 'vaginal itching': 44,
 'vaginal pain': 109,
 'vaginal redness': 110,
 'vomiting': 40,
 'vomiting blood': 84,
 'warts': 205,
 'weakness': 111,
 'weight gain': 102,
 'wheezing': 88,
 'white discharge from eye': 32,
 'wrist pain': 55,
 'wrist swelling': 58
 }

diseases_list = {
 0: 'actinic keratosis',
 1: 'acute bronchiolitis',
 2: 'acute bronchitis',
 3: 'acute bronchospasm',
 4: 'acute kidney injury',
 5: 'acute pancreatitis',
 6: 'acute sinusitis',
 7: 'allergy',
 8: 'angina',
 9: 'anxiety',
 10: 'appendicitis',
 11: 'arthritis of the hip',
 12: 'asthma',
 13: 'benign prostatic hyperplasia (bph)',
 14: 'brachial neuritis',
 15: 'bursitis',
 16: 'carpal tunnel syndrome',
 17: 'cholecystitis',
 18: 'chronic back pain',
 19: 'chronic constipation',
 20: 'chronic obstructive pulmonary disease (copd)',
 21: 'common cold',
 22: 'complex regional pain syndrome',
 23: 'concussion',
 24: 'conjunctivitis',
 25: 'conjunctivitis due to allergy',
 26: 'contact dermatitis',
 27: 'cornea infection',
 28: 'croup',
 29: 'cystitis',
 30: 'degenerative disc disease',
 31: 'dental caries',
 32: 'depression',
 33: 'developmental disability',
 34: 'diaper rash',
 35: 'diverticulitis',
 36: 'drug reaction',
 37: 'ear drum damage',
 38: 'eczema',
 39: 'esophagitis',
 40: 'eustachian tube dysfunction (ear disorder)',
 41: 'fungal infection of the hair',
 42: 'gallstone',
 43: 'gastrointestinal hemorrhage',
 44: 'gout',
 45: 'gum disease',
 46: 'heart attack',
 47: 'heart failure',
 48: 'hemorrhoids',
 49: 'herniated disk',
 50: 'hiatal hernia',
 51: 'hyperemesis gravidarum',
 52: 'hypertensive heart disease',
 53: 'hypoglycemia',
 54: 'idiopathic excessive menstruation',
 55: 'idiopathic irregular menstrual cycle',
 56: 'idiopathic painful menstruation',
 57: 'infectious gastroenteritis',
 58: 'injury to the arm',
 59: 'injury to the leg',
 60: 'injury to the trunk',
 61: 'liver disease',
 62: 'macular degeneration',
 63: 'marijuana abuse',
 64: 'multiple sclerosis',
 65: 'noninfectious gastroenteritis',
 66: 'nose disorder',
 67: 'obstructive sleep apnea (osa)',
 68: "otitis externa (swimmer's ear)",
 69: 'otitis media',
 70: 'pain after an operation',
 71: 'panic disorder',
 72: 'pelvic inflammatory disease',
 73: 'peripheral nerve disorder',
 74: 'personality disorder',
 75: 'pneumonia',
 76: 'problem during pregnancy',
 77: 'psoriasis',
 78: 'pyogenic skin infection',
 79: 'rectal disorder',
 80: 'schizophrenia',
 81: 'seasonal allergies (hay fever)',
 82: 'sebaceous cyst',
 83: 'sepsis',
 84: 'sickle cell crisis',
 85: 'sinus bradycardia',
 86: 'skin pigmentation disorder',
 87: 'skin polyp',
 88: 'spinal stenosis',
 89: 'spondylosis',
 90: 'spontaneous abortion',
 91: 'sprain or strain',
 92: 'strep throat',
 93: 'stye',
 94: 'temporary or benign blood in urine',
 95: 'threatened pregnancy',
 96: 'urinary tract infection',
 97: 'vaginal cyst',
 98: 'vaginitis',
 99: 'vulvodynia'
}

svc = pickle.load(open('Model/rf.pkl','rb'))


precautions = pd.read_csv("Model/Datasets/precautions.csv")
workout = pd.read_csv("Model/Datasets/workout.csv")
description = pd.read_csv("Model/Datasets/description.csv")
medications = pd.read_csv('Model/Datasets/medications.csv')
diets = pd.read_csv("Model/Datasets/diets.csv")


def helper(dis):
 dis = dis.lower()

 # Description
 desc = description[description['Disease'].str.lower() == dis]['Description']
 desc = desc.tolist()

 # Precautions
 pre = precautions[precautions['Disease'].str.lower() == dis][
  ['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
 pre = pre.values.tolist()

 # Medications
 med = medications[medications['Disease'].str.lower() == dis]['Medication']
 med_string = med.values[0]
 med = ast.literal_eval(med_string)

 # Diets
 die = diets[diets['Disease'].str.lower() == dis]['Diet']
 die_string = die.values[0]
 die = ast.literal_eval(die_string)

 # Workouts
 wrkout = workout[workout['Disease'].str.lower() == dis]['Workouts']
 wrkout_string = wrkout.values[0]
 wrkout = ast.literal_eval(wrkout_string)

 return {
  'description': desc,
  'precautions': pre[0] if pre else [],
  'medications': med,
  'diets': die,
  'workout': wrkout
 }

# Model Prediction function
def get_predicted_value(patient_symptoms):
 input_vector = np.zeros(len(symptoms_dict))
 for item in patient_symptoms:
  input_vector[symptoms_dict[item]] = 1
 return diseases_list[svc.predict([input_vector])[0]]


def get_details(symptoms):
 if isinstance(symptoms, str):
  user_symptoms = [s.strip("[]' ") for s in symptoms.split(',')]
 else:
  user_symptoms = [s.strip() for s in symptoms]

 predicted_disease = get_predicted_value(user_symptoms)
 data = helper(predicted_disease)

 return {
  'symptoms': user_symptoms,
  'disease': predicted_disease,
  'description': data['description'],
  'precautions': data['precautions'],
  'medications': data['medications'],
  'diets': data['diets'],
  'workout': data['workout']
 }

if __name__ == '__main__':
 symptoms = input("Enter your symptoms.......")
 data = get_details(symptoms)

 print(data['symptoms'])
 print(data['disease'])
 print(data['description'])
 print(data['precautions'])
 print(data['medications'])
 print(data['diets'])
 print(data['workout'])
 # len(symptoms_dict)

