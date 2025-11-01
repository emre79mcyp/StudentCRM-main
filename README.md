# University of Kyrenia - Student Portal

A Django-based administrative portal system for managing student information at the University of Kyrenia. Built with Django 4.2 and enhanced with Jazzmin for a modern, intuitive admin interface.

## Overview

The Student Portal is a robust backend management system designed to streamline student data administration. It features an enhanced admin interface with Jazzmin, data import/export capabilities, and comprehensive student management tools.

## Features

- **Modern Admin Interface**: Enhanced with Jazzmin for improved UX/UI
- **Student Management**: Comprehensive student data management system
- **Data Import/Export**: Support for Excel and other formats via django-import-export
- **SQLite Database**: Lightweight default setup (PostgreSQL supported)
- **Media Management**: Integrated media file handling
- **Dark Mode Support**: Toggle between light and dark themes
- **Responsive Design**: Works on desktop and mobile devices
- **Search Functionality**: Quick search for student records

## Tech Stack

- **Framework**: Django 4.2
- **Database**: SQLite3 (PostgreSQL optional)
- **Admin Interface**: Jazzmin 2.6.0
- **Data Management**: django-import-export 3.2.0
- **Image Processing**: Pillow 9.5.0
- **Code Formatting**: Black 23.3.0
- **ASGI Server**: Asgiref 3.6.0

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository** (if applicable)
   ```bash
   git clone <repository-url>
   cd student-portal
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser account**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files** (for production)
   ```bash
   python manage.py collectstatic
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the portal**
   - Admin Interface: `http://localhost:8000/admin`
   - Login with your superuser credentials

## Project Structure

```
core/
├── settings.py          # Django configuration and settings
├── urls.py              # URL routing configuration
├── wsgi.py              # WSGI application entry point
└── asgi.py              # ASGI application entry point

student/
├── models.py            # Student data models
├── admin.py             # Admin interface customization
├── views.py             # View logic
├── urls.py              # App URL routing
└── migrations/          # Database migrations

manage.py                # Django command-line utility
requirements.txt         # Python dependencies
media/                   # User-uploaded files
db.sqlite3               # SQLite database (default)
```

## Configuration

### Database Setup

**Default (SQLite):**
The project uses SQLite by default, which requires no additional setup.

**PostgreSQL (Optional):**
To use PostgreSQL, uncomment and configure the DATABASES section in `settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "<db_name>",
        "USER": "<db_username>",
        "PASSWORD": "<password>",
        "HOST": "<db_hostname_or_ip>",
        "PORT": "<db_port>",
    }
}
```

Then install the PostgreSQL adapter:
```bash
pip install psycopg2-binary
```

### Jazzmin Customization

Jazzmin settings are configured in `settings.py`:

- **Site Title**: "Portal Admin"
- **Site Header**: "Portal"
- **Site Brand**: "University of Kyrenia"
- **Theme**: Flatly (with Darkly dark mode option)
- **Search Model**: Student records

You can customize colors, logos, and layout by modifying the `JAZZMIN_SETTINGS` dictionary.

### Static & Media Files

- **STATIC_URL**: `/static/` - CSS, JavaScript, and other static assets
- **MEDIA_URL**: `/media/` - User-uploaded files
- **MEDIA_ROOT**: `media/` directory in project root

## Common Commands

```bash
# Create new app
python manage.py startapp <app_name>

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Access Django shell
python manage.py shell

# Format code with Black
black .

# Export data
python manage.py export_admin <app.Model>

# Import data
python manage.py import_admin <app.Model>
```

## Admin Interface Features

The Jazzmin-enhanced admin interface provides:

- **Dashboard**: Quick overview of student data
- **Search Bar**: Fast student lookup
- **Dark Mode**: Toggle between light and dark themes
- **Custom Icons**: Font Awesome icons for navigation
- **Responsive Layout**: Optimized for all screen sizes
- **Import/Export**: Bulk data operations

## Environment Variables

For production, set these environment variables:

```bash
DEBUG=False
SECRET_KEY=<your-secret-key>
ALLOWED_HOSTS=yourdomain.com
```

**⚠️ Security Warning**: Never expose your SECRET_KEY in version control. Use environment variables or `.env` files.

## API Routes

- **Admin Dashboard**: `/admin/`
- **Media Files**: `/media/<filename>`
- **Static Files**: `/static/<filename>`

## Installed Apps

- `jazzmin` - Enhanced admin interface
- `django.contrib.admin` - Django admin
- `django.contrib.auth` - Authentication system
- `django.contrib.contenttypes` - Content type framework
- `django.contrib.sessions` - Session management
- `django.contrib.messages` - Messaging framework
- `django.contrib.staticfiles` - Static file management
- `import_export` - Data import/export functionality
- `student` - Custom student app

## Dependencies

All project dependencies are listed in `requirements.txt`. Key packages include:

- Django 4.2
- django-jazzmin 2.6.0
- django-import-export 3.2.0
- Pillow 9.5.0
- Black 23.3.0
- PyYAML 6.0

## Troubleshooting

**Issue**: "No module named 'django'"
- **Solution**: Ensure virtual environment is activated and dependencies installed: `pip install -r requirements.txt`

**Issue**: "SECRET_KEY exposed" warning
- **Solution**: Change the SECRET_KEY in settings.py for production and use environment variables

**Issue**: Database migration errors
- **Solution**: Run `python manage.py migrate` to apply all pending migrations

**Issue**: Static files not loading
- **Solution**: Run `python manage.py collectstatic` and ensure STATIC_URL is configured correctly

## Production Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS` with your domain
3. Use a production-grade database (PostgreSQL recommended)
4. Use a production WSGI server (Gunicorn, uWSGI)
5. Implement SSL/HTTPS
6. Set up proper logging and error handling
7. Use environment variables for sensitive data

## Security Notes

- Keep `SECRET_KEY` confidential
- Always use `DEBUG = False` in production
- Configure `ALLOWED_HOSTS` properly
- Use HTTPS for all connections
- Implement proper authentication and permissions
- Regularly update dependencies

## Support & Contact

For issues, questions, or contributions, please refer to the project documentation or contact the development team.

## License

This project is proprietary to the University of Kyrenia. All rights reserved.

---

**Students Portal Ltd**
