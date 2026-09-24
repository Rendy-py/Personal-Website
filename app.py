from flask import Flask, render_template

app = Flask(__name__)

# Halaman Home
@app.route('/')
def home():
    return render_template('index.html')

# Halaman Projects
@app.route('/projects')
def projects():
    # Daftar project lu. Tinggal ganti nama, desc, dan link gambarnya nanti
    my_projects = [
        {"name": "Nusantara 7 AUV",
         "desc": "Led a team in the end-to-end development of an Autonomous Underwater Vehicle (AUV) from the ground up, overseeing system design, software development, hardware-software integration, testing, and deployment for the Singapore AUV Challenge (SAUVC). Developed closed-loop control systems using PID tuning to achieve stable and responsive vehicle motion, integrated computer vision for visual-based navigation, and utilized a CMPS12 digital compass for precise heading estimation and orientation control. Additionally, configured and integrated acoustic pinger systems to enable accurate underwater distance detection, obstacle avoidance, and enhanced spatial awareness during autonomous operations.",
         "image": "asset/sauvc.jpeg"},

        {"name": "Pelamis 8 ASV",
         "desc": "Architected and developed the complete software framework for an autonomous surface vessel from scratch, encompassing system automation, thruster allocation, and programmatic vessel control. Developed and integrated data telemetry systems to enable real-time monitoring, diagnostics, and operational control, while implementing advanced computer vision capabilities for autonomous perception. Optimized vessel navigation and maneuverability through extensive PID tuning and control-system refinement, ensuring stable, precise, and reliable autonomous surface operations.",
         "image": "asset/KKI.jpeg"},

        {"name": "YOLO Hand Tracking",
         "desc": "Servo etc...",
         "image": "https://via.placeholder.com/300x200?text=Project+Gamma"},

        {"name": "Underwater Acoustic Side-Scan Sonar Analysis",
         "desc": "Conducted secondary data analysis on a pre-existing 2021 hydrographic survey dataset collected for submarine optical cable installation using SonarWiz 8. Performed advanced quantitative acoustic analysis using Continuous Wavelet Transform (CWT) and amplitude analysis to isolate, characterize, and classify specific seabed features. Extracted and evaluated acoustic signatures from the provided bathymetric and topographic data to identify potential subsea anomalies, demonstrating strong proficiency in digital signal processing, acoustic data interpretation, and hydrographic survey analysis.",
         "image": "https://via.placeholder.com/300x200?text=Project+Delta"},
    ]
    return render_template('projects.html', projects=my_projects)

if __name__ == '__main__':
    app.run(debug=True)
