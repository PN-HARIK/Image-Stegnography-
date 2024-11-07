from PIL import Image
import stepic
import os
import streamlit as st

def file_exists(path):
    return os.path.isfile(path)

def is_supported_image(path):
    return any(path.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg'])

def encrypt_image(img, msg):
    encoded_img = stepic.encode(img, msg.encode())
    return encoded_img

def decrypt_image(img):
    return stepic.decode(img)

def main():
    st.title("Image Encryption and Decryption")
    
    mode = st.radio("Choose Mode", ["Encrypt", "Decrypt"])
    
    if mode == "Encrypt":
        img_upload = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
        msg = st.text_area("Enter Message")
        
        if img_upload and msg:
            img = Image.open(img_upload)
            
            if st.button("Encrypt"):
                enc_img = encrypt_image(img, msg)
                enc_img.save("enc_image.png")
                st.image(enc_img, caption="Encrypted Image", use_container_width=True)
                st.success("Encryption Done!")
                st.download_button("Download Encrypted Image", data=open("enc_image.png", "rb"), file_name="enc_image.png", mime="image/png")
    
    elif mode == "Decrypt":
        enc_img_upload = st.file_uploader("Upload Encrypted Image", type=["png", "jpg", "jpeg"])
        
        if enc_img_upload:
            img = Image.open(enc_img_upload)
            
            if st.button("Decrypt"):
                decoded_msg = decrypt_image(img)
                
                if decoded_msg:
                    st.success("Decryption Done!")
                    st.text_area("Decoded Message", decoded_msg, height=200)
                else:
                    st.warning("No hidden message.")

if __name__ == "__main__":
    main()
