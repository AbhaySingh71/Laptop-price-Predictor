
<h1>💻 Laptop Price Predictor 🧠🔍</h1>

<p>This project is a <strong>Machine Learning-based Laptop Price Predictor</strong> that allows users to input laptop specifications and receive an estimated price.</p>

<blockquote><strong>🔧 Main Objective:</strong> Showcase Docker-based ML model deployment and API hosting.</blockquote>

<h2>🚀 Features</h2>
<ul>
  <li>🧼 Cleaned and processed dataset</li>
  <li>🔍 EDA & Feature Engineering</li>
  <li>🔁 Trained regression model</li>
  <li>📦 Flask-based API</li>
  <li>🐳 Dockerized deployment</li>
  <li>📊 Jupyter Notebook</li>
</ul>

<h2>🧠 Tech Stack</h2>
<ul>
  <li>Python</li>
  <li>Pandas, NumPy, Scikit-Learn</li>
  <li>Flask</li>
  <li>Docker</li>
  <li>Jupyter Notebook</li>
</ul>

<h2>📁 Project Structure</h2>
<pre><code>├── app.py
├── Dockerfile
├── df.pkl
├── laptop_data.csv
├── pipeline.pkl
├── requirements.txt
├── Laptop_price_Predictor.ipynb</code></pre>

<h2>📦 Docker Deployment</h2>
<p><strong>1. Build Docker Image</strong></p>
<pre><code>docker build -t laptop-price-predictor .</code></pre>

<p><strong>2. Run Docker Container</strong></p>
<pre><code>docker run -p 5000:5000 laptop-price-predictor</code></pre>

<p>Visit <code>http://localhost:5000</code> to interact with the app.</p>

<h2>🌐 Deployed App</h2>
<ul>
  <li><strong>Live Demo</strong>: <a href="https://laptop-price-prediction-abhaysingh.streamlit.app/"></a></li>
  <li><strong>DockerHub</strong>: <a href="https://hub.docker.com/repository/docker/abhaysingh71/lappy/general">https://hub.docker.com/r/abhaysingh71/laptop-price-predictor</a></li>
</ul>

<h2>⚡ Sample API Usage</h2>
<pre><code>POST /predict</code></pre>

<p><strong>Input:</strong></p>
<pre><code>{
  "Brand": "Dell",
  "Processor": "Intel Core i5",
  "RAM": "8 GB",
  "Storage": "512 GB SSD",
  "GPU": "Intel Iris Xe",
  "OS": "Windows 11"
}</code></pre>

<p><strong>Output:</strong></p>
<pre><code>{
  "predicted_price": 58999
}</code></pre>

<h2>📌 Note</h2>
<p>This project is primarily designed to demonstrate <strong>Dockerized ML Model Deployment</strong>. It is for educational use.</p>

<h2>👨‍💻 Author</h2>
<p><strong>Abhay Singh</strong><br/>
<a href="https://github.com/AbhaySingh71">GitHub</a> |
<a href="https://www.linkedin.com/in/abhay-singh-050a5b293">LinkedIn</a></p>

<h2>📜 License</h2>
<p>MIT License</p>

</body>
</html>
