# GamifiED
AI-powered gamified learning platform for students and teachers

**Team XP Innovators:**
- Ishrath Tabassum
- Mekala Madhu Mitha

**Technologies Used:**
- Python & Streamlit for the frontend UI.
- Firebase Realtime Database for backend data storage.
- Altair for interactive data visualization.
- Requests and Lottie for animations and enhanced UI effects.
- Custom Python modules for XP logic, quiz handling, and badge assignment.

**How to run:**
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/GamifiED.git
    cd GamifiED
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    .\venv\Scripts\activate   # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up Firebase credentials:
    - Create a Firebase project.
    - Obtain your Firebase config and authentication keys.
    - Place them in `firebase_config.py`.

5. Run the app:
    ```bash
    streamlit run main.py
    ```

**Key Features:**
**User Authentication**: Secure login and user management with Firebase.
- **Personalized Dashboards**: Track XP, badges, progress charts, and assigned courses.
- **Dynamic Quizzes**: Level-based quizzes with automated grading and detailed feedback.
- **Gamification**: XP accumulation, badges (Beginner to Master), and level progress bars.
- **Progress Visualization**: XP over time charts and visual progress indicators.
- **AI-Driven Feedback**: Automated feedback highlighting strengths and areas for improvement (with plans for enhanced NLP-based feedback).
- **Responsive UI**: Modern, gaming-themed design with custom fonts and animations.

**How AI Is Used:**
- Automated quiz grading with instant feedback.
- Personalized feedback per question, indicating correct/incorrect responses.
- Future plans include integrating advanced NLP models for detailed explanations, adaptive quizzes, and personalized learning paths.

**Future Enhancements**
- Implement AI-powered adaptive learning paths.
- Use NLP models to generate rich, personalized feedback.
- Add social features like leaderboards and peer challenges.
- Mobile app support for learning on-the-go.
- Analytics dashboard for instructors.

**Contributing**
Contributions are welcome! Feel free to:
- Report bugs or request features via Issues.
- Fork the repo and create pull requests with improvements.
- Suggest ideas for AI enhancements or gamification.


