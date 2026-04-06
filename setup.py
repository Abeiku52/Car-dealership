#!/usr/bin/env python3
"""
Setup script for Cars Dealership Application
This script helps set up the Django project for development and testing
"""

import os
import sys
import subprocess
import django
from pathlib import Path

def run_command(command, cwd=None):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            cwd=cwd,
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error: {e.stderr}")
        return None

def setup_django():
    """Set up Django project"""
    print("Setting up Django project...")
    
    # Change to server directory
    server_dir = Path(__file__).parent / 'server'
    
    # Add server directory to Python path
    sys.path.insert(0, str(server_dir))
    
    # Set Django settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
    
    try:
        django.setup()
        print("✓ Django setup completed")
        return True
    except Exception as e:
        print(f"✗ Django setup failed: {e}")
        return False

def create_migrations():
    """Create Django migrations"""
    print("Creating Django migrations...")
    
    server_dir = Path(__file__).parent / 'server'
    
    # Create migrations
    result = run_command('python3 manage.py makemigrations', cwd=server_dir)
    if result is not None:
        print("✓ Migrations created")
        return True
    else:
        print("✗ Failed to create migrations")
        return False

def apply_migrations():
    """Apply Django migrations"""
    print("Applying Django migrations...")
    
    server_dir = Path(__file__).parent / 'server'
    
    # Apply migrations
    result = run_command('python3 manage.py migrate', cwd=server_dir)
    if result is not None:
        print("✓ Migrations applied")
        return True
    else:
        print("✗ Failed to apply migrations")
        return False

def create_superuser():
    """Create Django superuser"""
    print("Creating Django superuser...")
    
    server_dir = Path(__file__).parent / 'server'
    
    # Create superuser with default credentials
    create_superuser_command = '''
from django.contrib.auth.models import User;
User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
'''
    
    result = run_command(f'python3 manage.py shell -c "{create_superuser_command}"', cwd=server_dir)
    if result is not None:
        print("✓ Superuser created (username: admin, password: admin123)")
        return True
    else:
        print("✗ Failed to create superuser")
        return False

def populate_sample_data():
    """Populate database with sample data"""
    print("Populating database with sample data...")
    
    server_dir = Path(__file__).parent / 'server'
    
    # Run populate_data command
    result = run_command('python3 manage.py populate_data', cwd=server_dir)
    if result is not None:
        print("✓ Sample data populated")
        return True
    else:
        print("✗ Failed to populate sample data")
        return False

def collect_static():
    """Collect static files"""
    print("Collecting static files...")
    
    server_dir = Path(__file__).parent / 'server'
    
    # Collect static files
    result = run_command('python3 manage.py collectstatic --noinput', cwd=server_dir)
    if result is not None:
        print("✓ Static files collected")
        return True
    else:
        print("✗ Failed to collect static files")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up Cars Dealership Application")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path('server/manage.py').exists():
        print("✗ Error: manage.py not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Setup steps
    steps = [
        ("Django Setup", setup_django),
        ("Create Migrations", create_migrations),
        ("Apply Migrations", apply_migrations),
        ("Create Superuser", create_superuser),
        ("Populate Sample Data", populate_sample_data),
        ("Collect Static Files", collect_static),
    ]
    
    success_count = 0
    
    for step_name, step_func in steps:
        print(f"\n📋 {step_name}")
        if step_func():
            success_count += 1
        else:
            print(f"⚠️  {step_name} failed, but continuing...")
    
    print("\n" + "=" * 50)
    print(f"✅ Setup completed! ({success_count}/{len(steps)} steps successful)")
    
    if success_count == len(steps):
        print("\n🎉 Your Cars Dealership application is ready!")
        print("\nNext steps:")
        print("1. Start the Django server: cd server && python3 manage.py runserver")
        print("2. Start the sentiment analysis service: cd sentiment && python3 app.py")
        print("3. Visit http://127.0.0.1:8000/ to view the application")
        print("4. Visit http://127.0.0.1:8000/admin/ to access the admin panel")
        print("   - Username: admin")
        print("   - Password: admin123")
    else:
        print("\n⚠️  Some setup steps failed. Please check the errors above.")
        print("You may need to install dependencies first:")
        print("pip3 install -r requirements.txt")

if __name__ == '__main__':
    main()