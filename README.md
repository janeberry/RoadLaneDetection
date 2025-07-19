# Steps to detect Road Lane

# 1. The Sample Photo
<img width="463" height="264" alt="Image" src="https://github.com/user-attachments/assets/874cd61f-4310-434a-a900-c026d5df1058" />

# 2. Preprocessing the Image

<p> 
  <li>convert the image to the grayscale.</li>
  <li>divide the image into tow parts: top half, bottom half</li>
  <li>apply Gaussian blur to the top half because we don't need it</li>
</p>
<img width="507" height="295" alt="Image" src="https://github.com/user-attachments/assets/a58d2b08-154c-41bd-bba3-c8a1e5c30dfb" />

# 3. Canny Edge Detection

<p> I kept preprocessing the image untill get the best edges. </p>
<img width="506" height="297" alt="Image" src="https://github.com/user-attachments/assets/086f9ad3-12b5-4874-b233-f4eeb2fc9601" />

# 4. Apply HoughLines
<img width="505" height="296" alt="Image" src="https://github.com/user-attachments/assets/bdd0d5e9-8074-4234-9cf3-94a3d5a4645c" />

