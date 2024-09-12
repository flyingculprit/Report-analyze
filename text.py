from googletrans import Translator

# Initialize the translator
translator = Translator()

# Function to translate text
def translate_text(text, dest_language='ta'):
    translation = translator.translate(text, dest=dest_language)
    return translation.text

# Example usage
text_to_translate = "How are you?"
translated_text = translate_text(text_to_translate, dest_language='ta')

print(f"Original: {text_to_translate}")
print(f"Translated: {translated_text}")




# import requests

# API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
# headers = {"Authorization": "Bearer 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"}

# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()
	
# output = query({
# 	"inputs": "provided all these are good or any symtoms for the disease  ---JAMMI SCANS DEPARTMENT OF FETAL MEDICINE No:16 Vaidhyaraman Street , Tnagar Patient name Age/Sex_|31 Years / Female Patient ID Visitno__|1 Referred by Visit date LMP date 02/03/2023, LMP EDD: 07/12/2023[12W 1D] OB - First Trimester Scan Report Indication(s) First trimester screening Real time B-mode ultrasonography of gravid uterus done. Route: Transabdominal and Transvaginal Single intrauterine gestation Medical notes Blood group: A1B+ve Height : 159 cms Weight : 48.2kgs Marital History: 4 years Consanguinity : NCM Menstrual History : Regular Gravida: 2 Para: 1 Live: 1 Abortion : 0 Significant previous obstetric details : Nil Medical / Surgical History : Lscs. Maternal Cervix measured 3.10 cm in length. Right Uterine 1.8 2 (57%) Left Uterine 1.4 He4+— (29%) Mean PI 1.6 H-e— (45%) Fetus Survey Placenta - Anterior Liquor - Normal Fetal activity present Cardiac activity present Fetal heart rate - 154 bpm Biometry (mm) CRL 59, 12W 3D +—#— (54%) BPD 21, 13W 2D H+ (81%) HC 75.43,13W 1D +—+#4(65%) AC 58.14,12W4D + —+#4(71%) PC PNDT : 1284/2016 FOR APPOINTMENTS KINDLY CONTACT US AT 7904513421 / 7338771733 Page #1 - 26/05/23 11:29 AM",
# })

# print(output)