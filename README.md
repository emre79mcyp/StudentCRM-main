Features & Technical Implementation
1. Customized Django Admin as an Application
Description: Leverages the django-jazzmin package to completely transform the standard Django Admin into a modern, branded, and user-friendly portal for administrative staff. This goes far beyond basic CRUD operations.

Relevance: Shows the ability to build practical, internal tools without needing a separate frontend, a common requirement in many businesses.

2. Data Model Design & Relationships
Description: Implemented a clean, relational data model with a Student entity and a related Document model for file uploads. This demonstrates understanding of database relationships (ForeignKey) and structured data design.

Relevance: Core skill for backend development and test automation (designing test data models).

3. Advanced Admin Features
Inline Model Editing: Integrated DocumentInline to allow adding and editing a student's documents directly from the student detail page, streamlining the user workflow.

Data Import/Export: Integrated django-import-export to allow administrators to bulk import student data from or export to CSV/XLSX files, a critical feature for data migration and reporting.

Enhanced Usability: Configured list_display, search_fields, and list_display_links to make the admin interface efficient and practical for daily use.

4. File Management
Description: Configured Django to handle file uploads (FileField) for student documents, with automatic saving to the media/ directory and serving them during development.

Relevance: Demonstrates experience with handling non-database resources, a common task in web applications.

🛠️ Technology Stack
Backend Framework: Django

Admin Theme & Customization: django-jazzmin

Data Import/Export: django-import-export

Database: SQLite (Development) / PostgreSQL (Production-ready in settings)

Storage: Local file system handling for media uploads
core/
├── student/                 # Main application
│   ├── migrations/         # Database migration files
│   ├── models.py          # Defines Student & Document models
│   ├── admin.py           # Customizes the Admin interface for the app
│   └── apps.py
├── core/
│   ├── settings.py        # Project configuration (Jazzmin, apps, media)
│   ├── urls.py           # Routes; serves admin and media files
│   └── wsgi.py
├── media/                 # Directory for uploaded student documents
├── db.sqlite3            # Database (not in version control)
└── manage.py
