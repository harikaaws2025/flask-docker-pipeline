# Flask Docker Jenkins Pipeline 🚀

A simple Python Flask app with a login page — containerized and automated using Jenkins.

## 💻 Run Locally

```bash
docker build -t flask-docker-pipeline .
docker run -p 5000:5000 flask-docker-pipeline

---

## 🔧 Jenkins Setup Instructions

### 🧩 Install These Plugins
- **Pipeline**
- **Git**
- **Docker Pipeline**
- **Credentials Binding**
- **Blue Ocean** *(optional)*

---

### 🔐 Add DockerHub Credentials
**Jenkins → Manage Jenkins → Credentials → Global → Add Credentials**

| Field | Value |
|--------|--------|
| Kind | Username & Password |
| ID | `dockerhub-creds` |
| Username | your DockerHub username |
| Password | your DockerHub password or token |

---

### 🧰 Set Up Docker on Jenkins Host

If Jenkins runs on Linux/EC2:
```bash
sudo apt update
sudo apt install docker.io -y

sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
