<h1><b>TrailBliss Travelers</b></h1>

Welcome to **TrailBliss Travelers**, your gateway to exploring the world and making unforgettable memories. 

---

## Table of Contents

1. [Website Features](#website-features)
2. [Pages Overview](#pages-overview)
   - [Home](#home)
   - [About](#about)
   - [Contact](#contact)
   - [Destinations](#destinations)
   - [Signup](#signup)
   - [Login](#login)
3. [Project Structure](#project-structure)
4. [Technologies Used](#technologies-used)
5. [How to Run the Project](#how-to-run-the-project)
6. [Challenges Faced](#challenges-faced)

---

<h3>Website Features</h3> 

- **Responsive Design:** Accessible on both desktop and mobile devices.
- **User-Friendly Navigation:** Intuitive navigation across all pages.
- **Interactive Forms:** A simulated signup and login system.
- **Dynamic Content:** Destination highlights with beautiful visuals.
- **Engaging Content:** Information on why you should choose TrailBliss Travelers.

---

## Pages Overview

### Home
- **Purpose:** Provide a welcoming entry point with a hero section to inspire exploration.
- **Highlights:**
  - Tagline: "Explore the World with Us."
  - Call-to-action buttons for "Explore Destinations" and "Book Now."

### About
- **Purpose:** Share the mission, vision, and unique value of TrailBliss Travelers.
- **Highlights:**
  - "Why Choose Us" section with key features: Handpicked Destinations, 24/7 Support, and Affordable Packages.
  - Beautiful visuals to enhance storytelling.

### Contact
- **Purpose:** Allow users to reach out for inquiries or feedback.
- **Highlights:**
  - Contact form with fields for name, email, phone, and message.
  - Embedded Google Maps for easy office location identification.
  - Links to social media platforms.

### Destinations
- **Purpose:** Highlight featured destinations with curated travel recommendations.
- **Highlights:**
  - Grid layout displaying destinations like Paris, Maldives, Kyoto, and Iceland.
  - Hover effects for interactivity.
  - "View Details" button for each destination.

### Signup
- **Purpose:** Simulated signup for users to "create an account."
- **Highlights:**
  - Form fields for username, email, and password.
  - Responsive design for better usability.

### Login
- **Purpose:** Simulated login for returning users.
- **Highlights:**
  - Form fields for username and password.
  - Error messages for invalid credentials.

---

## Project Structure

```
TrailBliss/
|-- app/
|   |-- static/
|   |   |-- css/
|   |   |   |-- styles.css
|   |   |-- images/
|   |-- templates/
|   |   |-- base.html
|   |   |-- home.html
|   |   |-- about.html
|   |   |-- destinations.html
|   |   |-- contact.html
|   |   |-- signup.html
|   |   |-- login.html
|-- app.py
|-- requirements.txt
|-- README.md
```

---

## Technologies Used

- **Frontend:** HTML5, CSS3
- **Backend:** Flask (Python)
- **Icons:** Boxicons
- **Styling Frameworks:** Custom CSS with Flexbox and Grid

---

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/trailbliss-travelers.git
   ```

2. Navigate to the project directory:
   ```bash
   cd trailbliss-travelers
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

---

## Challenges Faced

1. **Consistency in Navigation:**
   - **Challenge:** Maintaining a consistent navigation bar across all pages.
   - **Solution:** Used a shared `base.html` template with dynamic Flask routes.

2. **Responsive Design:**
   - **Challenge:** Ensuring the website works seamlessly on all devices.
   - **Solution:** Implemented CSS Flexbox and Media Queries for adaptability.

3. **Simulating User System:**
   - **Challenge:** Simulating login/signup without a database.
   - **Solution:** Used hardcoded logic in Flask to validate inputs.

---

## Future Enhancements

- Integrate a database for persistent user management.
- Add dynamic destination pages with detailed itineraries.
- Implement a real-time chat support system.
