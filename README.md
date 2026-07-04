<div align="center">
  <h1>📸 Image Cartoonifying & Road Lane Detection</h1>
  
  <p>
    A Computer Vision project implementing image processing filters to cartoonify real-world images and utilizing the Hough Transform for autonomous road lane detection.
  </p>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
</p>
</div>

---

## 📖 Overview

This repository contains the implementation of **Assignment 1** for the Computer Vision course. The project introduces foundational image processing and feature extraction techniques through two main applications:
1. **Image Cartoonifying:** Combining edge detection and bilateral filtering to transform real-world photographs into comic-book-style drawings.
2. **Road Lane Detection:** Using Canny edge detection and the Hough Transform to identify and highlight road lanes in driving dashcam footage.

---

## 🏗️ Implementation Details

### Part I: Image Cartoonifying
The goal is to flatten regions of color while drastically enhancing distinct edges to simulate a hand-drawn cartoon effect.

1. **Black-and-White Sketch Generation:**
   * **Grayscale Conversion:** Converts the default BGR image to Grayscale.
   * **Noise Reduction:** Applies a **Median Filter** to remove noise while preserving sharp edges.
   * **Edge Detection:** Uses a **Laplacian Filter** to detect edges, as it closely mimics human sketch strokes.
   * **Thresholding:** A binary threshold is applied to the Laplacian output to ensure edges are strictly solid black or white.
2. **Color Painting Generation:**
   * Applies a **Bilateral Filter** to smooth flat color regions while keeping edges intact. 
   * *Optimization Trick:* To improve processing speed, the algorithm downsizes the image and applies multiple small bilateral filters (e.g., $9 \times 9$) iteratively rather than a single massive, computationally expensive filter.
3. **Overlay & Final Effect:**
   * The binary sketch mask is overlaid onto the bilaterally filtered "painting", replacing the painting's pixels with black lines wherever strong edges exist.

### Part II: Road Lane Detection (Hough Transform)
Detecting lines corresponding to lane boundaries using parametric voting space.

1. **Preprocessing & Smoothing:** Applies a 2D Median filter to blur the image and reduce noise.
2. **Edge Detection:** Utilizes the **Canny Edge Detection** algorithm with high thresholds to isolate strong structural edges.
3. **Region of Interest (ROI) Extraction:**  A predefined polygon mask is applied to the edge image to crop out the sky, dashboard, and off-road scenery, leaving only the road surface.
4. **Hough Transform Accumulation:**
   * Maps edge pixels into the $(\rho, \theta)$ parameter space based on the normal line equation:
     $$x \cos \theta + y \sin \theta = \rho$$
   * Plots the accumulator array as an image to visualize the voting operation.
5. **Post-Processing & Refinement:**
   * Searches the $(\rho, \theta)$-space for the highest accumulator peaks.
   * Applies **Non-Maximum Suppression** to eliminate redundant or overlapping lines, producing clean, singular lane boundary coordinates.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.8+
* OpenCV (`cv2`)
* NumPy
* Matplotlib (for visualizing intermediate steps and accumulator arrays)

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/OmarHani4306/cv-cartoonify-and-lane-detection.git] (https://github.com/OmarHani4306/cv-cartoonify-and-lane-detection.git)
   cd cv-cartoonify-lane-detection
   ```

2. **Install dependencies:**
   ```bash
   pip install numpy opencv-python matplotlib
   ```

3. **Run the Cartoonifier script:**
   ```bash
   python src/cartoonify.py --image data/sample.jpg
   ```

4. **Run the Lane Detection script:**
   ```bash
   python src/lane_detection.py --image data/road.jpg
   ```

---

## 🎓 Academic Context

**Alexandria University** | Faculty of Engineering | Computer and Systems Engineering Department

* **Course:** CSE: Computer Vision (Fall 2025)
* **Instructor:** Eng. Shereen Elkordi
