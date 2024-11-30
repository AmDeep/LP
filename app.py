import streamlit as st

# Set up page config
st.set_page_config(
    page_title="TryGuide.ai",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Navigation Bar
st.markdown(
    """
    <style>
        .navbar {font-size: 18px; font-weight: bold; color: #ffffff;}
        .navbar a {text-decoration: none; color: #ffffff; padding: 10px;}
        .navbar a:hover {background-color: #0073e6;}
        .navbar-container {display: flex; justify-content: space-between; align-items: center; background-color: #000000; padding: 10px 20px;}
        .navbar-container .logo {font-size: 24px; font-weight: bold; color: #ffffff;}
    </style>
    <div class="navbar-container">
        <div class="logo">TryGuide.ai</div>
        <div class="navbar">
            <a href="#platform">Platform</a>
            <a href="#use-cases">Use Cases</a>
            <a href="#pricing">Pricing</a>
            <a href="#security">Security</a>
            <a href="#contact">Contact</a>
            <a href="#waitlist">Join Waitlist</a>
            <a href="https://calendly.com/phil-hong-guideai/30min" target="_blank">Book Demo</a>
        </div>
    </div>
    """, unsafe_allow_html=True
)

# Main Headline and Subheadline
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="font-size: 48px; color: #333333; font-weight: bold;">AI-Powered Data Extraction and Automation—Secure and Reliable</h1>
        <h3 style="font-size: 24px; color: #555555;">Upload your PDFs, verify data accuracy, and let AI agents take action—trusted by teams for 99% accuracy.</h3>
        <div style="margin-top: 20px;">
            <a href="#waitlist" style="padding: 15px 30px; background-color: #0073e6; color: white; text-decoration: none; border-radius: 5px; margin-right: 20px;">Join the Waitlist</a>
            <a href="https://calendly.com/phil-hong-guideai/30min" target="_blank" style="padding: 15px 30px; background-color: #0073e6; color: white; text-decoration: none; border-radius: 5px;">Book a Demo</a>
        </div>
    </div>
    """, unsafe_allow_html=True
)

# Key Features Section
st.markdown(
    """
    <h2 style="text-align: center; color: #333333;">Smart AI-Powered Solutions for Your Data Needs</h2>
    <ul style="font-size: 18px; color: #555555;">
        <li><strong>Upload to Our Secure Platform</strong>: Process PDFs, images, or text documents with ease.</li>
        <li><strong>Verify the Extracted Data</strong>: Ensure every detail is accurate with simple validation tools.</li>
        <li><strong>Automate Actions</strong>: Trigger AI agents to handle repetitive workflows like updating databases or generating reports.</li>
    </ul>
    """, unsafe_allow_html=True
)

# How It Works Section
st.markdown(
    """
    <h2 style="text-align: center; color: #333333;">Three Simple Steps to Automate Your Workflow</h2>
    <ol style="font-size: 18px; color: #555555;">
        <li><strong>Upload</strong>: Upload any file—PDFs, scanned images, or text documents.</li>
        <li><strong>Verify</strong>: Review and confirm extracted data for peace of mind.</li>
        <li><strong>Act</strong>: AI agents take over, automating tedious processes instantly.</li>
    </ol>
    """, unsafe_allow_html=True
)

# Use Cases Section
st.markdown(
    """
    <h2 style="text-align: center; color: #333333;">Use Cases</h2>
    <ul style="font-size: 18px; color: #555555;">
        <li><strong>Invoices</strong>: Extract totals, due dates, and payment details.</li>
        <li><strong>Contracts</strong>: Identify parties, terms, and renewal dates.</li>
        <li><strong>Receipts</strong>: Categorize expenses with precision.</li>
        <li><strong>Custom Documents</strong>: Define your own fields and data types.</li>
    </ul>
    """, unsafe_allow_html=True
)

# Security Section
st.markdown(
    """
    <h2 style="text-align: center; color: #333333;">Your Data, Fully Protected</h2>
    <ul style="font-size: 18px; color: #555555;">
        <li><strong>GDPR Compliant</strong>: We adhere to the strictest data protection regulations.</li>
        <li><strong>No Training on Your Data</strong>: Your files remain confidential—never used to train AI.</li>
        <li><strong>Fully Encrypted</strong>: All communication and data storage are secure with advanced encryption.</li>
        <li><strong>Built for Enterprise</strong>: Scalable and secure solutions tailored to your needs.</li>
    </ul>
    """, unsafe_allow_html=True
)

# Why Choose TryGuide.ai
st.markdown(
    """
    <h2 style="text-align: center; color: #333333;">Why Choose TryGuide.ai?</h2>
    <ul style="font-size: 18px; color: #555555;">
        <li><strong>99% Accuracy</strong>: Powered by cutting-edge large language models.</li>
        <li><strong>Custom Solutions</strong>: White-glove onboarding and tailored configurations.</li>
        <li><strong>Proven Team</strong>: Built by AI engineers behind products used by millions.</li>
    </ul>
    """, unsafe_allow_html=True
)

# Closing CTA Section
st.markdown(
    """
    <div style="text-align: center;">
        <h2 style="color: #333333;">Transform Your Document Workflows Today</h2>
        <a href="#waitlist" style="padding: 15px 30px; background-color: #0073e6; color: white; text-decoration: none; border-radius: 5px; margin-right: 20px;">Join the Waitlist</a>
        <a href="https://calendly.com/phil-hong-guideai/30min" target="_blank" style="padding: 15px 30px; background-color: #0073e6; color: white; text-decoration: none; border-radius: 5px;">See It in Action—Book a Demo</a>
    </div>
    """, unsafe_allow_html=True
)

# Footer Section
st.markdown(
    """
    <div style="background-color: #333333; color: white; padding: 20px 0; text-align: center;">
        <p style="font-size: 16px; margin: 0;">
            <a href="#about" style="color: white; text-decoration: none; padding: 10px;">About</a> |
            <a href="#platform" style="color: white; text-decoration: none; padding: 10px;">Platform</a> |
            <a href="#pricing" style="color: white; text-decoration: none; padding: 10px;">Pricing</a> |
            <a href="#privacy" style="color: white; text-decoration: none; padding: 10px;">Privacy Policy</a> |
            <a href="#terms" style="color: white; text-decoration: none; padding: 10px;">Terms of Service</a>
        </p>
    </div>
    """, unsafe_allow_html=True
)
