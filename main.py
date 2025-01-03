import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "I am a physiotherapist and would like you to suggest treatment plan for patients based on my inputs. I can use this as baseline to update further before sharing with the patient. Kindly suggest the treatment plan without disclaimers and in a format that I can simply edit/update and share.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "## Patient Name: [Patient Name]\n## Date: [Date]\n## Diagnosis: [Diagnosis]\n\n**Subjective:** [Patient's reported symptoms, limitations, and goals. Include pain levels, aggravating/easing factors, and relevant history.]\n\n**Objective:** [Your findings from the physical examination. Include range of motion, strength, posture, special tests, and palpation findings.]\n\n**Assessment:** [Your clinical impression based on the subjective and objective findings. Summarize the key issues and link them to the diagnosis.]\n\n**Plan:**\n\n**Short-Term Goals (e.g., 2 weeks):**\n* [Specific, Measurable, Achievable, Relevant, and Time-bound (SMART) goal 1, e.g., Reduce pain from 7/10 to 4/10 during daily activities.]\n* [SMART goal 2, e.g., Increase active shoulder flexion range of motion by 15 degrees.]\n* [SMART goal 3, e.g., Improve understanding of proper body mechanics for lifting.]\n\n\n**Long-Term Goals (e.g., 6 weeks):**\n* [SMART goal 1, e.g., Return to pain-free participation in recreational sports.]\n* [SMART goal 2, e.g., Achieve full and pain-free shoulder range of motion.]\n* [SMART goal 3, e.g., Independently perform a home exercise program.]\n\n**Treatment:**\n\n**Frequency:** [e.g., 2x/week for 6 weeks]\n\n**Interventions:**\n* **Manual Therapy:** [e.g., Soft tissue mobilization to upper trapezius, joint mobilizations to thoracic spine]\n* **Therapeutic Exercise:** [e.g., Scapular stabilization exercises, shoulder strengthening exercises, stretching of pectoral muscles, core strengthening]\n* **Modalities:** [e.g., Heat therapy prior to exercise, ice therapy after exercise]\n* **Patient Education:** [e.g., Posture education, activity modification advice, pain neuroscience education]\n* **Home Exercise Program:** [List specific exercises with sets, reps, and frequency.  Include clear descriptions or images/links to videos.]\n\n\n**Progression:** [Describe how treatment will progress over time. E.g., Increase exercise intensity and complexity as tolerated. Introduce functional exercises.]\n\n**Re-assessment:** [Specify when you will re-assess the patient's progress, e.g., after 2 weeks.]\n\n\n**Prognosis:** [Your prediction of the expected outcome of treatment, e.g., Good prognosis for full recovery.]\n\n\n\n---\n\n\n**Example Home Exercise Program:**\n\n1. **Scapular Retractions:**  3 sets of 15 repetitions, twice daily.  Sit upright, squeeze shoulder blades together, hold for 5 seconds, relax.\n2. **Pendulum Exercises:** 3 sets of 10 repetitions in each direction, twice daily. Lean forward with good posture, let the affected arm hang down, and swing it gently forward and backward, side to side, and in circles.\n\n\nThis is a template and should be adapted to each individual patient's specific needs and condition.  Remember to update the bracketed information with the relevant patient details.\n",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)