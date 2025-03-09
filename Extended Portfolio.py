import http.server
import socketserver
import webbrowser
import threading

# HTML Content for the webpage
HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Extended Portfolio</title>
    <style>
        /* General body and header styles */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        header {
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 30px 0;
            font-size: 28px;
            text-transform: uppercase;
        }

        /* Container and content sections */
        .container {
            width: 80%;
            margin: 20px auto;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        .fade-in {
            animation: fadeIn 2s ease-out;
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }

        /* About Me Section */
        .about-me {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }
        .about-me img {
            border-radius: 50%;
            width: 150px;
            height: 150px;
            margin-bottom: 20px;
        }
        .about-me h1 {
            font-size: 36px;
        }
        .about-me p {
            font-size: 20px;
            color: #555;
        }

        /* Skills Section */
        .skills-list {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
        }
        .skills-list li {
            background-color: #4CAF50;
            color: white;
            padding: 12px 25px;
            border-radius: 5px;
            font-size: 18px;
            transition: transform 0.3s ease-in-out;
        }
        .skills-list li:hover {
            transform: scale(1.1);
            background-color: #45a049;
        }

        /* Projects Section */
        .projects-section {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-top: 30px;
        }
        .project-card {
            background-color: white;
            padding: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
            transition: transform 0.3s ease-in-out;
        }
        .project-card:hover {
            transform: scale(1.05);
        }
        .project-card h3 {
            color: #4CAF50;
        }
        .project-card p {
            color: #555;
        }

        /* Experience and Education Sections */
        .section-title {
            text-align: center;
            font-size: 28px;
            margin-top: 40px;
            color: #333;
        }
        .experience, .education {
            margin-top: 20px;
        }
        .experience-item, .education-item {
            padding: 15px;
            margin-bottom: 20px;
            background-color: #fff;
            border-left: 5px solid #4CAF50;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        }

        /* Testimonial Section */
        .testimonials {
            display: flex;
            justify-content: space-around;
            margin-top: 40px;
        }
        .testimonial {
            width: 30%;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease-in-out;
        }
        .testimonial:hover {
            transform: scale(1.05);
        }
        .testimonial h4 {
            color: #4CAF50;
        }
        .testimonial p {
            color: #555;
        }

        /* Contact Form Section */
        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .contact-form button {
            background-color: #4CAF50;
            color: white;
            padding: 12px 25px;
            font-size: 18px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
        }
        .contact-form button:hover {
            background-color: #45a049;
        }

        /* Footer */
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 15px;
            font-size: 14px;
            margin-top: 40px;
        }

    </style>
</head>
<body>

<header>
    <h1>My Extended Portfolio</h1>
    <p>Explore my work, skills, and journey</p>
</header>

<!-- About Me Section -->
<div class="container fade-in">
    <div class="about-me">
        <img src="https://via.placeholder.com/150" alt="Profile Image">
        <h1>Welcome to My Portfolio</h1>
        <p>Hello! My name is Josh Dominic Benny and I'm a passionate software engineer who loves solving problems and building innovative solutions. This portfolio showcases my skills, experience, and projects.</p>
    </div>
</div>

<!-- Skills Section -->
<div class="container fade-in">
    <h2 class="section-title">Skills</h2>
    <ul class="skills-list">
        <li>Python</li>
        <li>JavaScript</li>
        <li>HTML & CSS</li>
        <li>React</li>
        <li>Node.js</li>
        <li>SQL</li>
        <li>Machine Learning</li>
        <li>Data Visualization</li>
        <li>Docker</li>
    </ul>
</div>

<!-- Projects Section -->
<div class="container fade-in">
    <h2 class="section-title">Projects</h2>
    <div class="projects-section">
        <div class="project-card">
            <h3>Portfolio Website</h3>
            <p>A personal portfolio to showcase my projects and skills in a user-friendly way.</p>
            <a href="https://github.com" target="_blank">View Project</a>
        </div>
        <div class="project-card">
            <h3>Weather App</h3>
            <p>A web app that allows users to check weather data based on location.</p>
            <a href="https://github.com" target="_blank">View Project</a>
        </div>
        <div class="project-card">
            <h3>Task Manager</h3>
            <p>A to-do list application to manage daily tasks and projects.</p>
            <a href="https://github.com" target="_blank">View Project</a>
        </div>
    </div>
</div>

<!-- Experience Section -->
<div class="container fade-in">
    <h2 class="section-title">Experience</h2>
    <div class="experience">
        <div class="experience-item">
            <h3>Software Engineer at Atlassian</h3>
            <p>June 2020 - Present</p>
            <p>Developed scalable and high-performance web applications using React and Node.js. Worked as a teams.</p>
        </div>
        <div class="experience-item">
            <h3>Intern Developer at Microsoft Ltd</h3>
            <p>January 2019 - May 2020</p>
            <p>Assisted in building internal tools and optimizing existing systems. Contributed to backend APIs and database management.</p>
        </div>
    </div>
</div>

<!-- Education Section -->
<div class="container fade-in">
    <h2 class="section-title">Education</h2>
    <div class="education">
        <div class="education-item">
            <h3>Bachelor of Computer Science</h3>
            <p>Queensland University of Technology, Graduated in 2027</p>
            <p>Specialized in Software Engineering and Data Structures.</p>
        </div>
    </div>
</div>

<!-- Testimonials Section -->
<div class="container fade-in">
    <h2 class="section-title">Testimonials</h2>
    <div class="testimonials">
        <div class="testimonial">
            <h4>Josh Benny</h4>
            <p>"An amazing developer! Highly skilled and very professional. Truly an asset to the team."</p>
        </div>
        <div class="testimonial">
            <h4>Geo Benny</h4>
            <p>"Fantastic work ethic and great problem-solving skills. Helped us deliver a critical project on time."</p>
        </div>
    </div>
</div>

<!-- Contact Form Section -->
<div class="container fade-in contact-form">
    <h2>Contact Me</h2>
    <form action="javascript:void(0);">
        <input type="text" id="name" placeholder="Your Name" required>
        <input type="email" id="email" placeholder="Your Email" required>
        <textarea id="message" rows="5" placeholder="Your Message" required></textarea>
        <button type="submit" onclick="validateForm()">Send Message</button>
    </form>
</div>

<!-- Footer -->
<footer>
    <p>&copy; 2025 My Portfolio | Designed with Love</p>
    <p>Follow me on <a href="https://twitter.com" style="color: #4CAF50;" target="_blank">Twitter</a> and <a href="https://github.com" style="color: #4CAF50;" target="_blank">GitHub</a></p>
</footer>

<script>
    function validateForm() {
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const message = document.getElementById("message").value;
        
        if (name === "" || email === "" || message === "") {
            alert("All fields are required.");
        } else {
            alert("Your message has been sent! Thanks for reaching out.");
        }
    }
</script>

</body>
</html>
"""

# Server Class to Serve the Page
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode("utf-8"))

# Run Server and Open Browser Automatically
def open_browser():
    webbrowser.open("http://localhost:8000")

def run_server():
    handler = CustomHandler
    httpd = socketserver.TCPServer(("", 8000), handler)
    print("Server started at http://localhost:8000")
    httpd.serve_forever()

# Run server in a separate thread to not block the main thread
server_thread = threading.Thread(target=run_server)
server_thread.start()

# Open the page in the default browser
open_browser()
