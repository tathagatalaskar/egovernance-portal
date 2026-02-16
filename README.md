# Tripura E-Governance Portal

A comprehensive web-based e-governance portal built to facilitate citizen services, complaint management, and document access. This project demonstrates modern web development practices with Python Flask, SQLite database, and responsive frontend design.

## 🌟 Project Overview

The Tripura E-Governance Portal is a citizen-centric web application that bridges the gap between government services and citizens. It provides an intuitive interface for:
- Filing and tracking complaints
- Requesting government services
- Downloading official documents
- Accessing emergency contacts
- Administrative dashboard for managing requests

**Developed by:** Tathagata Laskar  
**Tech Stack:** Python Flask, SQLite, HTML5, CSS3, JavaScript  
**Purpose:** Understanding e-governance architecture and building citizen-centric digital solutions

## ✨ Features

### Citizen Features
- **Home Dashboard**: Overview of services with quick access links
- **Complaint Management**: 
  - Submit complaints with detailed information
  - Receive unique tracking ID
  - Track complaint status in real-time
  - Department-wise categorization
- **Service Requests**:
  - Apply for various government certificates
  - Submit service applications online
  - Track request status
- **Document Portal**:
  - Download application forms
  - Access policy documents
  - View guidelines and brochures
- **Contact Information**:
  - Department contact details
  - Office hours and location
  - Emergency helpline numbers

### Admin Features
- **Secure Login**: Password-protected admin panel
- **Complaint Dashboard**: View all complaints with filters
- **Status Management**: Update complaint status (Pending/In Progress/Resolved/Closed)
- **Service Request Monitor**: Track all service requests
- **Real-time Updates**: Instant reflection of status changes

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**: Core programming language
- **Flask 2.3**: Lightweight web framework
- **Flask-SQLAlchemy 3.0**: Database ORM
- **SQLite**: Embedded database

### Frontend
- **HTML5**: Structure and markup
- **CSS3**: Styling with modern features (Grid, Flexbox)
- **JavaScript**: Client-side interactivity
- **Responsive Design**: Mobile-friendly interface

### Database Schema

**Complaint Model:**
```
- id (Primary Key)
- name (String)
- email (String)
- phone (String)
- department (String)
- subject (String)
- description (Text)
- status (String - default: 'Pending')
- date_submitted (DateTime)
```

**ServiceRequest Model:**
```
- id (Primary Key)
- name (String)
- email (String)
- phone (String)
- service_type (String)
- details (Text)
- status (String - default: 'Submitted')
- date_requested (DateTime)
```

## 📁 Project Structure

```
egovernance-portal/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── egovernance.db             # SQLite database (auto-created)
├── static/
│   └── style.css              # CSS stylesheet
├── templates/
│   ├── base.html              # Base template
│   ├── index.html             # Home page
│   ├── services.html          # Services listing
│   ├── complaint.html         # Complaint form
│   ├── track_complaint.html   # Track complaint
│   ├── service_request.html   # Service request form
│   ├── documents.html         # Documents page
│   ├── contact.html           # Contact information
│   ├── admin_login.html       # Admin login
│   └── admin.html             # Admin dashboard
└── README.md                  # This file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (for version control)

### Step 1: Clone the Repository
```bash
git clone https://github.com/tathagatacodes/egovernance-portal.git
cd egovernance-portal
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5001`

### Step 5: Access the Portal
- **Citizen Portal**: http://localhost:5001
- **Admin Panel**: http://localhost:5001/admin
  - Default password: `admin123` (⚠️ Change in production!)

## 📸 Screenshots

*(Add screenshots of your application here after running it)*

### Home Page
![Home Page](#)

### Complaint Form
![Complaint Form](#)

### Admin Dashboard
![Admin Dashboard](#)

## 🎯 Usage Guide

### For Citizens

1. **Filing a Complaint:**
   - Navigate to "File Complaint" page
   - Fill in personal details
   - Select relevant department
   - Provide subject and description
   - Submit and note down the tracking ID

2. **Tracking Complaint:**
   - Go to "Track Complaint" page
   - Enter your tracking ID
   - View current status and details

3. **Requesting Services:**
   - Browse available services
   - Click on desired service
   - Fill service request form
   - Submit and receive request ID

### For Administrators

1. **Login:**
   - Navigate to `/admin`
   - Enter password (default: admin123)

2. **Managing Complaints:**
   - View all complaints in dashboard
   - Update status using dropdown
   - Changes reflect immediately

## 🔒 Security Considerations

**Current Implementation (Demo):**
- Simple password-based admin authentication
- Session-based login state
- Form validation on both client and server side

**Production Recommendations:**
- Implement proper user authentication (Flask-Login)
- Use environment variables for secrets
- Add CSRF protection
- Implement rate limiting
- Use HTTPS
- Hash passwords (bcrypt/argon2)
- Add email verification

## 🔧 Configuration

### Changing Admin Password
Edit `app.py` line 109:
```python
if password == 'your-new-password':  # Change this
```

### Database Location
The SQLite database is created as `egovernance.db` in the project root. To change location:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your-path/database.db'
```

## 🧪 Testing

### Manual Testing Checklist
- [ ] Home page loads correctly
- [ ] All navigation links work
- [ ] Complaint form submission
- [ ] Complaint tracking with valid ID
- [ ] Invalid ID shows error
- [ ] Service request submission
- [ ] Admin login
- [ ] Admin can view complaints
- [ ] Admin can update status
- [ ] Status changes reflect on tracking

## 📈 Future Enhancements

- [ ] Email notifications for status updates
- [ ] SMS integration for tracking updates
- [ ] File upload for supporting documents
- [ ] Multi-language support (English/Hindi/Bengali)
- [ ] Advanced search and filters
- [ ] Export reports (PDF/Excel)
- [ ] User registration and login
- [ ] Payment gateway integration
- [ ] Mobile application
- [ ] Analytics dashboard
- [ ] API for third-party integration

## 🤝 Contributing

This is a learning project, but suggestions are welcome!

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

**Tathagata Laskar**
- GitHub: [@tathagatacodes](https://github.com/tathagatacodes)
- LinkedIn: [linkedin.com/in/tathagata-laskar](https://linkedin.com/in/tathagata-laskar)
- Email: 24BCS11358@cuchd.in

## 🙏 Acknowledgments

- Inspired by various Indian government e-governance initiatives
- Built as part of academic project at Chandigarh University
- Special thanks to NIC (National Informatics Centre) for e-governance inspiration

## 📞 Support

For issues, questions, or suggestions:
- Create an issue on GitHub
- Email: 24BCS11358@cuchd.in

---

**Note:** This is an educational project demonstrating e-governance concepts. For production deployment, additional security measures and scalability considerations are required.

**Project Status:** ✅ Active Development

Last Updated: February 2026
