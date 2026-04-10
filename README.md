YOLO-based Construction Safety Detection System using Streamlit

 🚧 Construction Safety Detection System (YOLOv8)

 📌 Project Overview
This project is a **YOLO-based Computer Vision System** designed to detect safety compliance at construction sites.  
It identifies objects such as:
- 👷 Person
- 🪖 Helmet / No Helmet
- 🦺 Safety Vest

The system helps improve **workplace safety monitoring** using AI.



🎯 Features
-  Object Detection using YOLOv8
-  Real-time inference (image-based)
-  Streamlit Web App deployment
-  Lightweight model (YOLOv8n)
-  Easy-to-use interface



🧠 Technologies Used
- Python
- Ultralytics YOLOv8
- OpenCV
- Streamlit
- NumPy
- PIL (Python Imaging Library)



 📂 Project Structure


Yolo_Object_Detection_Project/
│
├── app_streamlit.py        # Streamlit app
├── object_detection.ipynb  # Training notebook
├── README.md               # Project documentation
├── .gitignore              # Ignore unnecessary files



📊 Dataset
- Source: Roboflow
- Type: Construction Safety Dataset
- Format: YOLOv8 compatible



 ⚙️ Installation

### Step 1: Clone repository
```bash
git clone https://github.com/your-username/Yolo_Object_Detection_Project.git
cd Yolo_Object_Detection_Project
````

 Step 2: Install dependencies

```bash
pip install ultralytics streamlit opencv-python numpy pillow


 🚀 Run the Project

```bash
streamlit run app_streamlit.py


👉 Open browser:

http://localhost:8501


 🖼️ How It Works

1. Upload an image
2. Model detects safety violations
3. Output image with bounding boxes is displayed

⚠️ Notes

Model file (`.pt`) is not included due to size limitations
 Dataset is not uploaded to GitHub



 🧪 Results

Successfully detects:

   Helmet / No Helmet
   Person
   Safety compliance

 📸 Output Example
<img width="1600" height="812" alt="image" src="https://github.com/user-attachments/assets/3706e6ea-28e1-4a11-976b-2fd770210022" />

<img width="1600" height="807" alt="image" src="https://github.com/user-attachments/assets/f4824cf8-acb9-42a8-9ea2-5c56beb81faa" />

 🎓 Academic Use

This project is developed as part of:
Lab Assignment – YOLO Multi-Task Vision System



👩‍💻 Author

Vaishnavi Thorave

 ⭐ Future Improvements

 🔹 Real-time webcam detection
 🔹 Confidence score display
 🔹 Cloud deployment
 🔹 Mobile app integration

 📌 Conclusion

This project demonstrates the use of **YOLOv8 for real-world safety applications**, providing an efficient and scalable solution for construction site monitoring.

