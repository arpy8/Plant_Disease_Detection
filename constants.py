MODEl_PATH = 'weights/plant_disease_classifier.h5'
FRONT_PAGE = """
<body style="font-family: Arial, sans-serif; color: #333; font-size: 16px;">
    <p>Welcome to the "Plant Disease Detection using CNN" Streamlit web application. This tool is designed to assist you in identifying the health status of your plants with the help of a Convolutional Neural Network (CNN). Whether you are a home gardener or a farmer, early detection of plant diseases can make a significant difference in preserving the well-being of your plants and optimizing crop yields.</p>
    <h2>How It Works</h2>
    <ol>
        <li><strong>Upload an Image:</strong> To get started, simply upload an image of your plant. The image should be clear and centered on the plant.</li>
        <li><strong>Prediction:</strong> Once you've uploaded an image, click the "Predict" button. Our pre-trained CNN model will analyze the image to determine whether the plant is "Healthy," affected by "Powdery Mildew," or has signs of "Rust."</li>
        <li><strong>Confidence Score:</strong> The application will provide you with a confidence score, indicating how sure the model is about its prediction.</li>
    </ol>
    <h2>Why Use This App?</h2>
    <ul>
        <li><strong>Early Disease Detection:</strong> Detecting plant diseases early can help prevent the spread of diseases and reduce crop losses.</li>
        <li><strong>Easy to Use:</strong> You don't need to be an expert in plant pathology. This user-friendly tool simplifies the process of disease detection.</li>
        <li><strong>Quick Results:</strong> In just a few seconds, you'll receive a classification result with a confidence score.</li>
    </ul>
    <h2>About</h2>
    <p>This web application is built using Streamlit and powered by a deep learning model. It offers a user-friendly interface for plant disease detection, making it accessible to anyone interested in plant health.</p>
    <h2>Get Started</h2>
    <p>To begin using this application, follow these steps:</p>
    <ol>
        <li>Click the "Upload an Image" button in the sidebar.</li>
        <li>Select an image of your plant from your device.</li>
        <li>Click the "Predict" button to see the classification result.</li>
    </ol>
    <p>Whether you are a professional farmer or a hobbyist gardener, this tool can help you keep your plants healthy and thriving. Try it out and make informed decisions about plant care!</p>
    <h2>Acknowledgments</h2>
    <p>We acknowledge the efforts of the open-source community in developing and sharing the model used in this application. This tool would not be possible without their contributions.</p>
    <p>If you have any feedback or suggestions for improving this application, we welcome your input. Together, we can help plants thrive and promote sustainable agriculture.</p>
    <p>Thank you for using the "Plant Disease Detection using CNN" web app!</p>
</body>
"""