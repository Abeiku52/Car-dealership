# Car Dealership Application

A comprehensive full-stack web application built with Django backend and React frontend for managing car dealerships, reviews, and user authentication.

## Project Name: Cars Dealership Platform

## Overview

This application serves as a national car retailer platform in the U.S., providing a responsive web application that displays dealership branches and allows users to view and submit reviews. The platform includes user authentication, dealer management, review systems with sentiment analysis, and comprehensive admin functionality.

## Technology Stack

- **Backend**: Django (Python)
- **Frontend**: React.js
- **Database**: SQLite (development), PostgreSQL (production)
- **Authentication**: Django built-in authentication system
- **Deployment**: IBM Cloud Code Engine with Docker and Kubernetes
- **CI/CD**: GitHub Actions
- **Additional Services**: 
  - Node.js microservices
  - MongoDB for reviews
  - Flask for sentiment analysis

## Key Features

### User Management
- User registration with comprehensive form (Username, First Name, Last Name, Email, Password)
- Secure login/logout functionality
- Admin panel access for management

### Dealer Management
- Display all dealerships across the nation
- Filter dealers by state (e.g., Kansas)
- Individual dealer detail pages
- Dealer contact information and location details

### Review System
- Submit reviews for specific dealers
- View all reviews for each dealer
- Sentiment analysis integration for review text
- Review management through admin interface

### Responsive Design
- Mobile-friendly interface
- Navigation bar with active states
- Professional About Us and Contact Us pages
- Consistent CSS styling across all pages

## API Endpoints

- `GET /api/dealers/` - Retrieve all dealers
- `GET /api/dealers/{id}/` - Get specific dealer details
- `GET /api/dealers/state/{state}/` - Filter dealers by state
- `GET /api/reviews/{dealer_id}/` - Get reviews for specific dealer
- `GET /api/cars/` - Retrieve all car makes and models
- `POST /api/sentiment/` - Analyze review sentiment
- `POST /api/auth/login/` - User authentication
- `POST /api/auth/logout/` - User logout

## Development Setup

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn
- Docker (for deployment)

### Installation Steps
1. Clone the repository
2. Set up Python virtual environment
3. Install Django dependencies
4. Set up React frontend
5. Configure database
6. Run development servers

## Deployment

The application is deployed using:
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Cloud Platform**: IBM Cloud Code Engine
- **CI/CD Pipeline**: GitHub Actions for automated deployment

## Project Structure

```
car-dealership/
├── server/                 # Django backend
│   ├── frontend/          # Static files and templates
│   │   ├── static/        # CSS, JS, images
│   │   └── src/           # React components
│   ├── dealerships/       # Django apps
│   └── manage.py
├── microservices/         # Node.js services
├── sentiment/             # Flask sentiment analysis
├── .github/workflows/     # CI/CD configuration
└── deployment/            # Kubernetes manifests
```

## Contributors

Full-stack Development Team - Cars Dealership Platform

## License

Educational Project - Full-stack Development Capstone