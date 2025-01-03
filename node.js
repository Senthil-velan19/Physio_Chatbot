const {
    GoogleGenerativeAI,
    HarmCategory,
    HarmBlockThreshold,
  } = require("@google/generative-ai");
  
  const apiKey = process.env.GEMINI_API_KEY;
  const genAI = new GoogleGenerativeAI(apiKey);
  
  const model = genAI.getGenerativeModel({
    model: "gemini-1.5-pro",
  });
  
  const generationConfig = {
    temperature: 1,
    topP: 0.95,
    topK: 40,
    maxOutputTokens: 8192,
    responseMimeType: "text/plain",
  };
  
  async function run() {
    const chatSession = model.startChat({
      generationConfig,
      history: [
        {
          role: "user",
          parts: [
            {text: "I am a physiotherapist and would like you to suggest treatment plan for patients based on my inputs. I can use this as baseline to update further before sharing with the patient. Kindly suggest the treatment plan without disclaimers and in a format that I can simply edit/update and share. keep it under 250 words "},
          ],
        },
        {
          role: "model",
          parts: [
            {text: "**Patient Name:** [Patient Name]\n**Date:** [Date]\n**Diagnosis:** [Diagnosis]\n\n**Goals:**\n* [Goal 1, e.g., Reduce pain to 3/10 on a visual analog scale]\n* [Goal 2, e.g., Improve range of motion in shoulder flexion to 160 degrees]\n* [Goal 3, e.g., Increase functional strength for independent dressing]\n\n**Treatment Plan:**\n\n**Phase 1 (Weeks 1-4): Pain Management and Range of Motion**\n\n* **Modalities:**  [e.g., Heat/Ice, Ultrasound, TENS] as needed for pain relief.\n* **Manual Therapy:** [e.g., Soft tissue mobilization, Joint mobilizations] to address tissue restrictions.\n* **Therapeutic Exercise:**  [e.g., Range of motion exercises, Gentle stretching] to improve mobility.\n* **Home Exercise Program:** [e.g., Pendulum exercises, Self-stretches] to be performed daily.\n\n\n**Phase 2 (Weeks 5-8): Strength and Functional Training**\n\n* **Therapeutic Exercise:** [e.g., Strengthening exercises using resistance bands/weights, Functional exercises] to improve strength and function.\n* **Neuromuscular Reeducation:** [e.g., Proprioceptive exercises, Balance training] to enhance motor control.\n* **Home Exercise Program:** Progression of home exercises with increased intensity and complexity.\n\n**Phase 3 (Weeks 9-12): Return to Activity**\n\n* **Therapeutic Exercise:** [e.g., Sport-specific training, Advanced strengthening]  to facilitate return to prior level of function.\n* **Activity Modification Education:**  [e.g.,  Ergonomics, Pacing techniques] to prevent recurrence.\n\n\n**Frequency:** [Frequency of visits, e.g., 2x/week]\n**Reassessment:** [Schedule for reassessment, e.g., Every 4 weeks]\n\n\n"},
          ],
        },
      ],
    });
  
    const result = await chatSession.sendMessage("INSERT_INPUT_HERE");
    console.log(result.response.text());
  }
  
  run();