🚗 ChalakSetu — Intelligent Mechanic Finder System
Find Nearby Mechanics. Get Help When Your Vehicle Breaks Down.

ChalakSetu is a location-based web application designed to help vehicle owners discover nearby mechanics when they experience unexpected vehicle breakdowns. The platform aims to reduce the time and effort required to find mechanical assistance, especially in unfamiliar locations and areas where access to organized roadside assistance may be limited.

Built using Python, Flask, HTML, CSS, JavaScript, and SQLite, ChalakSetu combines location-based discovery, email OTP authentication, password recovery, and a user-friendly interface in a lightweight web application.

The project focuses on solving a practical transportation problem through accessible web technology, with an architecture suitable for further development into a comprehensive roadside assistance platform.

📌 Table of Contents
Project Overview
The Problem
Our Solution
Key Features
Application Workflow
System Architecture
Technology Stack
Project Structure
Getting Started
Environment Configuration
Authentication and Security
Database Design
Deployment
Challenges and Engineering Considerations
Future Enhancements
Use Cases
Contributing
Author
License
🎯 Project Overview

Vehicle breakdowns can happen anywhere — on highways, in residential areas, in unfamiliar cities, or on roads where immediate mechanical assistance is difficult to find.

ChalakSetu is designed to simplify this situation by providing a digital platform for discovering nearby mechanics through a location-oriented interface.

Instead of depending entirely on word-of-mouth recommendations or manually searching for repair shops, users can access a web-based system intended to make mechanic discovery more convenient.

Project Highlights
📍 Location-based mechanic discovery
🔐 Email OTP-based signup and login
🔑 OTP-based password recovery
🖥️ Responsive and user-friendly web interface
🐍 Flask-based backend architecture
🗄️ Database integration using SQLite
🛡️ Password hashing and session-management considerations
☁️ Deployment using Render

Project Type: Full-Stack Web Application
Domain: Automotive Technology / Location-Based Services
Backend: Python and Flask
Database: SQLite
Deployment Platform: Render

🚨 The Problem

When a vehicle breaks down unexpectedly, finding a suitable mechanic can become a frustrating experience.

Common challenges include:

Difficulty identifying mechanics in an unfamiliar area.
Time wasted searching for nearby repair services.
Limited access to reliable mechanic information during emergencies.
Dependence on local contacts or unstructured online searches.
Inconvenient account recovery and authentication experiences on digital platforms.

These challenges can become particularly relevant for people travelling through unfamiliar towns, rural areas, or locations with limited roadside assistance infrastructure.

💡 Our Solution

ChalakSetu provides a web-based approach to mechanic discovery and account management.

The application brings together a location-oriented discovery experience and essential authentication features in one interface.

The system is designed around three core objectives:

Accessibility: Make mechanic discovery easier through a straightforward web interface.
Security: Provide account registration, login, and password recovery using email OTP verification and password hashing.
Extensibility: Maintain a Flask-based application structure that can support additional roadside assistance features in future versions.

The long-term vision is to evolve ChalakSetu into a broader roadside assistance ecosystem connecting vehicle owners with nearby service providers.

✨ Key Features
📍 1. Location-Based Mechanic Discovery

The core purpose of ChalakSetu is to help users discover mechanics based on their location.

Location-oriented mechanic discovery.
Designed for situations involving unexpected vehicle breakdowns.
A foundation for integrating map-based navigation and distance calculations.
Potential to expand to multiple cities and service areas.

Note: Actual GPS integration, map rendering, distance calculations, and live mechanic availability depend on the implementation configured in the deployed version.

🔐 2. Email OTP Authentication

ChalakSetu incorporates an email OTP-based authentication workflow.

Email verification during the applicable authentication process.
OTP-based verification flow.
Signup and login functionality.
A structured approach to account access and identity verification.

OTP expiry, resend limits, and attempt limits should be enforced by the backend where implemented.

🔑 3. Forgot Password and Account Recovery

Users can access an OTP-based password recovery workflow.

The intended process is:

Submit the registered email address.
Request a verification OTP.
Verify the OTP.
Set a new password after successful verification.

This provides a structured alternative to password recovery without relying on a permanently stored recovery code.

🎨 4. Interactive User Interface

The application is designed with a clean, accessible interface focused on usability.

Clear navigation and interface elements.
Interactive web components.
CSS-based styling and animations.
JavaScript for client-side interactions.
A foundation for responsive layouts across desktop and mobile screens.
🐍 5. Flask-Based Backend

The backend uses Python and Flask to handle application logic and web requests.

Route-based request handling.
Separation of frontend templates and backend logic where organized in the project.
Database integration.
Authentication-related workflows.
A lightweight foundation for extending the application with additional services.
🗄️ 6. Database Integration

SQLite provides a lightweight database option for application data.

Depending on the implemented schema, the database can support information such as:

User accounts.
Authentication-related records.
Mechanic profiles.
Location and service information.

Only the tables and fields present in the actual application should be considered implemented.

🛡️ 7. Security-Focused Design

Security is an important consideration in account-based applications.

ChalakSetu incorporates or is designed around:

Password hashing rather than plaintext password storage.
Session-based user access.
OTP-based verification workflows.
Server-side validation of sensitive operations.
Environment-based management of email credentials and secret keys.

Production readiness also requires appropriate session settings, HTTPS, rate limiting, input validation, and secure handling of OTPs.

🔄 Application Workflow

The following diagram illustrates the high-level application flow.

flowchart TD
    A[User Opens ChalakSetu] --> B{Existing Account?}

    B -->|No| C[Signup]
    C --> D[Email OTP Verification]
    D --> E[Account Access]

    B -->|Yes| F[Login]
    F --> G{Authentication Successful?}

    G -->|Yes| E
    G -->|No| H[Retry or Forgot Password]

    H --> I[Request Password Reset OTP]
    I --> J[Verify OTP]
    J --> K[Reset Password]
    K --> F

    E --> L[Access Application]
    L --> M[Discover Nearby Mechanics]

The diagram represents the intended user journey. Exact verification steps depend on the authentication flow implemented in the current codebase.

🏗️ System Architecture

ChalakSetu follows a web application architecture consisting of a presentation layer, a Flask backend, and a database layer.

flowchart TD
    U[User / Web Browser]

    subgraph Frontend
        H[HTML Templates]
        C[CSS Styling]
        JS[JavaScript Interactions]
    end

    subgraph Backend
        F[Flask Application]
        R[Routes and Application Logic]
        A[Authentication and Session Handling]
    end

    subgraph DataAndServices
        DB[(SQLite Database)]
        EM[Email OTP Service]
    end

    U --> H
    H --> C
    H --> JS
    H --> F
    F --> R
    R --> A
    A --> DB
    A --> EM
    F --> U
Architecture Components
Component	Responsibility
Frontend	Presents pages, forms, and interactive elements
Flask	Handles incoming requests and application logic
Authentication	Manages account access and verification workflows
SQLite	Stores application data according to the implemented schema
Email service	Supports OTP delivery where configured
Render	Provides the deployment environment

The architecture is intentionally lightweight and can be extended as the application's functionality grows.

🛠️ Technology Stack
Technology	Purpose
Python	Backend programming
Flask	Web application framework
HTML5	Page structure
CSS3	Styling, layouts, and animations
JavaScript	Client-side interactions
SQLite	Relational database
Email OTP	Account verification and password recovery
Git and GitHub	Version control and source-code management
Render	Application deployment
📂 Project Structure

The following is a reference structure for organizing the application. Adapt it to match the actual files in your repository.

ChalakSetu/
│
├── app.py                  # Flask application entry point
├── requirements.txt        # Python dependencies
├── .env                    # Local environment variables
├── .gitignore              # Files excluded from Git
│
├── templates/              # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   └── ...
│
├── static/                 # Frontend assets
│   ├── css/
│   ├── js/
│   └── images/
│
├── database/               # Database-related files, if separated
│
└── README.md               # Project documentation

Important: Do not create placeholder files merely to match this diagram. Document the actual repository structure when publishing the project.

🚀 Getting Started

Follow these steps to run the application locally.

Prerequisites

Install the following before starting:

Python 3.10 or a compatible version supported by your dependencies.
pip, the Python package installer.
Git.
A code editor such as Visual Studio Code.
1. Clone the Repository

Replace the placeholder below with your actual GitHub repository URL.

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ChalakSetu
2. Create a Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

Linux / macOS

python3 -m venv venv
source venv/bin/activate
3. Install Dependencies

If the repository includes a requirements.txt file:

pip install -r requirements.txt

If it does not, install the dependencies specified by your application and create a requirements file.

For example, Flask can be installed using:

pip install Flask

Email libraries and other packages depend on the implementation.

4. Configure Environment Variables

Create a local .env file if your application uses environment-based configuration.

Use the configuration section below as a reference, and match variable names to those actually read by your code.

5. Start the Application

For a Flask application whose entry point is app.py:

python app.py

Alternatively, if supported by the project:

flask --app app run --debug

Open the local URL displayed in the terminal, commonly:

http://127.0.0.1:5000

The exact startup command depends on how the Flask application is configured.

⚙️ Environment Configuration

Sensitive credentials should be stored outside the source code.

Example configuration template:

SECRET_KEY=replace_with_a_secure_random_secret
MAIL_SERVER=your_smtp_server
MAIL_PORT=587
MAIL_USERNAME=your_email_address
MAIL_PASSWORD=your_email_app_password

These are illustrative variable names, not a guarantee that the current application reads them directly.

Configuration Guidelines
Generate a unique, unpredictable Flask secret key.
Use an email provider's appropriate SMTP configuration.
Prefer app-specific email credentials when required by the provider.
Never commit .env files, email passwords, or secret keys to GitHub.
Add the necessary variables to Render's environment settings for deployment.

Example .gitignore entries:

.env
venv/
__pycache__/
*.py[cod]
instance/

If the project creates a local SQLite database, decide whether it should be version-controlled or generated during setup. Never publish a database containing real users' private information.

🔐 Authentication and Security

ChalakSetu uses an authentication-oriented design to support account access and recovery.

Password Protection

Passwords should be stored using a suitable password-hashing function, such as Werkzeug's password hashing utilities or another established password-hashing implementation.

Passwords should never be stored in plaintext.

OTP Verification

An OTP workflow should include the following protections:

Cryptographically secure OTP generation.
Short validity periods.
Server-side OTP verification.
Attempt limits and resend throttling.
Single-use verification codes.
Protection against account enumeration.
Secure storage of OTPs, preferably as hashes where appropriate.
Session Management

Session security should include:

A strong secret key.
Session invalidation after logout.
Appropriate cookie settings, including HttpOnly and Secure in HTTPS production deployments.
A suitable SameSite policy.
Reauthentication or session renewal after sensitive account changes.
Production Security Checklist

Debug mode disabled in production.

Secrets stored in environment variables.

HTTPS enabled for production traffic.

Password hashing verified in the codebase.

OTP expiry and attempt limits implemented.

Login and OTP endpoints protected against abuse.

Inputs validated on the server.

Sensitive data excluded from logs and public repositories.

Database persistence verified in the deployment environment.

These checks should be verified against the actual source code before describing the application as production-secure.

🗄️ Database Design

SQLite is suitable for a lightweight application and local development.

The database schema should reflect the actual entities used by ChalakSetu.

A potential logical model for future expansion is:

Entity	Example information
Users	User ID, email, password hash, account timestamps
Mechanics	Mechanic ID, name, contact details, service location
OTP Records	Email reference, verification purpose, expiry and usage status
Service Information	Supported repairs, service area, operating details

This is a conceptual model, not a claim that all these tables already exist in the repository.

Database Engineering Considerations
Enforce appropriate uniqueness constraints for user accounts.
Use parameterized database queries.
Validate records before insertion or modification.
Define appropriate relationships as the data model grows.
Plan database backups and persistence for deployment.
Consider PostgreSQL when the application requires a more robust shared database for concurrent users and persistent production data.
☁️ Deployment

ChalakSetu is associated with deployment on Render.

A typical Flask deployment requires:

A GitHub repository containing the application.
A valid dependency file.
A production WSGI server such as Gunicorn.
A Render web service configured with the appropriate build and start commands.
Environment variables configured in the deployment dashboard.
A database configuration suitable for persistent storage.

Example commands for a compatible Flask project:

Build command

pip install -r requirements.txt

Start command

gunicorn app:app

The command app:app assumes the Python module is app.py and the Flask application object is named app. Adjust it if your entry point or application object uses a different name.

Deployment Considerations

A local SQLite database stored on an ephemeral filesystem may not persist across certain deployment events. For production, verify Render's current storage configuration and ensure that database files are stored on suitable persistent storage or migrate to a managed database.

A successful deployment alone does not establish production readiness; authentication, data persistence, error handling, and security settings should also be tested.

🧠 Challenges and Engineering Considerations

Developing a mechanic discovery platform introduces several practical engineering considerations.

1. Location Accuracy

Location-based results depend on the accuracy of user coordinates, mechanic coordinates, and the mapping or geolocation service used.

2. Authentication Reliability

Email delivery delays, expired OTPs, repeated requests, and incorrect verification attempts require careful handling.

3. Database Persistence

The application must preserve required user and mechanic data across restarts and deployments.

4. User Experience During Breakdowns

A breakdown situation can be stressful. The interface should minimize unnecessary steps and present useful information clearly.

5. Scalability

As the number of users and mechanics increases, the application may need more efficient location queries, database indexing, caching, and a production-grade database.

These considerations provide a foundation for testing, improvement, and future system design.

🔮 Future Enhancements

ChalakSetu can be extended into a more comprehensive roadside assistance platform.

🗺️ Interactive Maps: Display mechanic locations using a mapping service.
📏 Distance Calculation: Sort mechanics by geographical distance.
📞 Direct Contact: Add calling and messaging options.
🚨 Emergency Assistance: Introduce a simplified breakdown request workflow.
🧰 Mechanic Profiles: Display services, experience, and contact information.
⭐ Ratings and Reviews: Allow users to share service feedback.
📡 Live Availability: Indicate whether mechanics are currently accepting requests.
📱 Mobile-Friendly Experience: Improve usability on smartphones and smaller screens.
🗃️ PostgreSQL Integration: Support a more scalable shared data layer.
🔔 Notifications: Add email or other appropriate status notifications.
🧭 Navigation Integration: Help users navigate to selected service providers.
🛠️ Service Request Tracking: Track a breakdown request from submission to completion.
🌐 Regional Expansion: Support more service areas and local mechanic networks.

These features represent potential development directions and should not be confused with functionality already implemented.

🌍 Use Cases

ChalakSetu is designed around practical situations where vehicle owners need to locate mechanical assistance.

Personal Vehicle Owners: Discover mechanic options when a vehicle develops a problem.

Long-Distance Travellers: Find service providers in unfamiliar areas.

Daily Commuters: Access a convenient digital starting point for locating mechanical assistance.

Local Mechanics: In a future provider-registration workflow, mechanics could publish service information and reach more potential customers.

Academic Demonstrations: Demonstrate the application of web development, authentication, database integration, and location-based service concepts in a practical project.

🤝 Contributing

Contributions and suggestions that improve usability, security, maintainability, and accessibility are welcome.

Fork the repository.
Create a feature branch.
Implement and test your changes.
Commit your work with a clear message.
Open a pull request describing the change.

Please avoid including credentials, personal information, or private user data in contributions.

👨‍💻 Author

Shreyansh Pandey

B.Tech — Computer Science and Information Technology

Interested in Python development, backend engineering, AI-powered systems, and practical technology solutions.

GitHub: @Shreyansh01234
📄 License

A license has not been specified in this documentation.

If you intend to make the project open source, consider adding an appropriate license file, such as the MIT License, after deciding which terms you want others to follow.

⭐ Support the Project

If you find ChalakSetu interesting, consider starring the repository on GitHub.

Your feedback and suggestions can help improve the project and its future development.

ChalakSetu — Connecting Vehicle Owners with the Roadside Assistance They Need. 🚗
