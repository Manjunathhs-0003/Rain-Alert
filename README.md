<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Rain Alert</h1>

  <h2>Overview</h2>
    <p>This Python script checks for rain predictions and sends a text alert using Twilio.</p>

  <h2>Features</h2>
    <ul>
        <li>Utilizes Twilio for text messaging.</li>
        <li>Provides real-time rain alerts based on weather data.</li>
    </ul>

   <h2>How to Use</h2>
    <ol>
        <li><strong>Setup:</strong>
            <ul>
                <li>Obtain API credentials:
                    <ul>
                        <li>Twilio Account SID and Authentication Token</li>
                        <li>OpenWeatherMap API Key</li>
                    </ul>
                </li>
                <li>Replace placeholders in the script with your credentials.</li>
            </ul>
        </li>
        <li><strong>Cloning the Repository:</strong>
            <p>Clone the repository to your local machine using the following command:</p>
            <pre><code>git clone https://github.com/Manjunathhs-0003/Rain-Alert.git</code></pre>
        </li>
        <li><strong>Usage:</strong>
            <ul>
                <li>Navigate to the cloned directory.</li>
                <li>Run the script: <code>python maint.py</code></li>
                <li>Receive a text message alert if rain is predicted for the specified location.</li>
            </ul>
        </li>
    </ol>

   <h2>Dependencies</h2>
    <ul>
        <li>Python 3.x</li>
        <li>requests</li>
        <li>twilio</li>
    </ul>

  <h2>Additional Note</h2>
    <p>If you want to automate this code to run automatically using PythonAnywhere or crontab, you can contact the project owner for assistance.</p>
</body>
</html>
