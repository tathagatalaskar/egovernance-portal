"""
Tripura E-Governance Portal
A simple government services web application
Author: Tathagata Laskar
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///egovernance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class Complaint(db.Model):
    """Model for storing citizen complaints"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Pending')
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Complaint {self.id}: {self.subject}>'

class ServiceRequest(db.Model):
    """Model for storing service requests"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    details = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Submitted')
    date_requested = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ServiceRequest {self.id}: {self.service_type}>'

# Routes
@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/services')
def services():
    """Services page"""
    return render_template('services.html')

@app.route('/complaint', methods=['GET', 'POST'])
def complaint():
    """Complaint submission page"""
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        department = request.form.get('department')
        subject = request.form.get('subject')
        description = request.form.get('description')
        
        # Create new complaint
        new_complaint = Complaint(
            name=name,
            email=email,
            phone=phone,
            department=department,
            subject=subject,
            description=description
        )
        
        # Add to database
        db.session.add(new_complaint)
        db.session.commit()
        
        flash(f'Complaint submitted successfully! Your tracking ID is: {new_complaint.id}', 'success')
        return redirect(url_for('complaint'))
    
    return render_template('complaint.html')

@app.route('/track-complaint', methods=['GET', 'POST'])
def track_complaint():
    """Track complaint status"""
    complaint_data = None
    if request.method == 'POST':
        complaint_id = request.form.get('complaint_id')
        complaint_data = Complaint.query.get(complaint_id)
        if not complaint_data:
            flash('No complaint found with this ID', 'error')
    
    return render_template('track_complaint.html', complaint=complaint_data)

@app.route('/service-request', methods=['GET', 'POST'])
def service_request():
    """Service request page"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        service_type = request.form.get('service_type')
        details = request.form.get('details')
        
        new_request = ServiceRequest(
            name=name,
            email=email,
            phone=phone,
            service_type=service_type,
            details=details
        )
        
        db.session.add(new_request)
        db.session.commit()
        
        flash(f'Service request submitted! Your request ID is: {new_request.id}', 'success')
        return redirect(url_for('service_request'))
    
    return render_template('service_request.html')

@app.route('/documents')
def documents():
    """Documents download page"""
    return render_template('documents.html')

@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    """Simple admin panel to view complaints"""
    # Simple password protection (in real project, use proper authentication)
    if request.method == 'POST':
        password = request.form.get('password')
        if password == 'admin123':  # Change this!
            session['admin_logged_in'] = True
            return redirect(url_for('admin'))
    
    if not session.get('admin_logged_in'):
        return render_template('admin_login.html')
    
    # Get all complaints and service requests
    complaints = Complaint.query.order_by(Complaint.date_submitted.desc()).all()
    service_requests = ServiceRequest.query.order_by(ServiceRequest.date_requested.desc()).all()
    
    return render_template('admin.html', complaints=complaints, service_requests=service_requests)

@app.route('/admin/logout')
def admin_logout():
    """Logout from admin panel"""
    session.pop('admin_logged_in', None)
    return redirect(url_for('index'))

@app.route('/admin/update-complaint/<int:complaint_id>', methods=['POST'])
def update_complaint(complaint_id):
    """Update complaint status"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin'))
    
    complaint = Complaint.query.get_or_404(complaint_id)
    new_status = request.form.get('status')
    complaint.status = new_status
    db.session.commit()
    
    flash('Complaint status updated!', 'success')
    return redirect(url_for('admin'))

# Initialize database
def init_db():
    """Initialize the database"""
    with app.app_context():
        db.create_all()
        print("Database initialized!")

if __name__ == '__main__':
    # Create database if it doesn't exist
    if not os.path.exists('egovernance.db'):
        init_db()
    
    # Run the app
    app.run(debug=True, host='0.0.0.0', port=5001)
