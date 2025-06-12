
<h1>💻 Laptop Price Predictor </h1>

<p>This project is a <strong>Machine Learning-based Laptop Price Predictor</strong> that takes laptop specifications as input and estimates its market price using ensemble-based ML models.</p>

<blockquote><strong>🔧 Main Objective:</strong> Showcase production-grade, Dockerized ML model deployment with ensemble learning techniques for real-world applications.</blockquote>

<h2>🚀 Features</h2>
<ul>
  <li>-> Cleaned & engineered dataset (`laptop_data.csv`)</li>
  <li>-> Exploratory Data Analysis & Feature Engineering</li>
  <li>-> Ensemble modeling with Voting & Stacking strategies</li>
  <li>-> Flask-based API for prediction</li>
  <li>-> Fully Dockerized for cross-platform deployment</li>
  <li>-> Interactive Streamlit App</li>
</ul>

<h2>🧠 Tech Stack</h2>
<ul>
  <li><strong>Languages:</strong> Python</li>
  <li><strong>Libraries:</strong> Pandas, NumPy, Scikit-learn, XGBoost</li>
  <li><strong>Modeling:</strong> Random Forest, Gradient Boosting, XGBoost, Extra Trees, Voting & Stacking</li>
  <li><strong>Deployment:</strong> Flask, Streamlit, Docker</li>
</ul>

<h2>📈 Machine Learning Strategy</h2>
<p>The price prediction model is built using multiple high-performance regressors, including:</p>
<ul>
  <li><strong>Random Forest Regressor</strong></li>
  <li><strong>Gradient Boosting Regressor</strong></li>
  <li><strong>XGBoost Regressor</strong></li>
  <li><strong>Extra Trees Regressor</strong></li>
</ul>

<p>These models are combined using:</p>
<ul>
  <li><strong>Voting Regressor</strong> – simple averaging of predictions from all base learners.</li>
  <li><strong>Stacking Regressor</strong> – a meta-model (Linear Regression) is trained on outputs of base models.</li>
</ul>

<p>This ensemble approach significantly improves generalization and accuracy, especially for tabular pricing data with mixed categorical and numerical features.</p>

<h2>📁 Project Structure</h2>
<pre><code>├── app.py                      # Flask API backend
├── Dockerfile                  # Docker configuration
├── df.pkl                      # Preprocessed data
├── laptop_data.csv             # Raw dataset
├── pipeline.pkl                # Trained ML pipeline (Voting/Stacking)
├── requirements.txt            # Python dependencies
├── Laptop_price_Predictor.ipynb # Full ML workflow notebook
</code></pre>

<h2> Docker Deployment</h2>
<p>This project is <strong>Docker-first</strong>. Docker ensures that the model can run in any environment without worrying about Python versions, dependencies, or system settings.</p>

<h3>🛠 Build Docker Image</h3>
<pre><code>docker build -t laptop-price-predictor .</code></pre>

<h3>🚀 Run Docker Container</h3>
<pre><code>docker run -p 5000:5000 laptop-price-predictor</code></pre>

<p>Once running, access the API locally via: <code>http://localhost:5000</code></p>

<h3>✅ Why Docker?</h3>
<ul>
  <li>Environment-independent deployments</li>
  <li>Fast setup and teardown</li>
  <li>Easy to host on cloud (AWS, GCP, Azure)</li>
  <li>Reproducibility for teams and CI/CD pipelines</li>
</ul>

<h2>🌐 Deployed App</h2>
<ul>
  <li><strong>Live Demo (Streamlit)</strong>: <a href="https://laptop-price-prediction-abhaysingh.streamlit.app/">https://laptop-price-prediction-abhaysingh.streamlit.app/</a></li>
  <li><strong>DockerHub</strong>: <a href="https://hub.docker.com/repository/docker/abhaysingh71/lappy/general">https://hub.docker.com/r/abhaysingh71/laptop-price-predictor</a></li>
</ul>

<h2> Sample API Usage</h2>
<pre><code>POST /predict</code></pre>

<p><strong>Sample Input JSON:</strong></p>
<pre><code>{
  "Brand": "Dell",
  "Processor": "Intel Core i5",
  "RAM": "8 GB",
  "Storage": "512 GB SSD",
  "GPU": "Intel Iris Xe",
  "OS": "Windows 11"
}</code></pre>

<p><strong>Sample Output:</strong></p>
<pre><code>{
  "predicted_price": 58999
}</code></pre>

<h2>📊 Visual Output (Streamlit)</h2>
<p>The Streamlit UI allows users to:</p>
<ul>
  <li>Select brand, processor, RAM, GPU, storage</li>
  <li>Get a real-time price prediction</li>
  <li>Understand model working in a simple form</li>
</ul>

<h2>📌 Note</h2>
<p>This project is built for educational and portfolio demonstration purposes. Model predictions are not intended for commercial use. The price estimation is based on past data and might not reflect current market fluctuations.</p>

<h2>👨‍💻 Author</h2>
<p><strong>Abhay Singh</strong><br/>
<a href="https://github.com/AbhaySingh71">GitHub</a> |
<a href="https://www.linkedin.com/in/abhay-singh-050a5b293">LinkedIn</a></p>

<h2>📜 License</h2>
<p>This project is licensed under the <strong>MIT License</strong>.</p>

</body>
</html>
