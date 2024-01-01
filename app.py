import streamlit as st
from PIL import Image

# from transformers import AutoProcessor, AutoModelForCausalLM
# import os

# processor = AutoProcessor.from_pretrained("microsoft/git-base-coco")
# model = AutoModelForCausalLM.from_pretrained("microsoft/git-base-coco")
#
#
# def generate_caption(image_path):
#     image = Image.open(image_path)
#
#     pixel_values = processor(images=image, return_tensors="pt").pixel_values
#     generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
#     generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
#
#     # Placeholder function for generating a caption
#     return generated_caption


def is_image_file(filename):
    # Check if the file has a valid image extension
    valid_extensions = ['.jpg', '.jpeg', '.png']
    return any(filename.lower().endswith(ext) for ext in valid_extensions)


def main():
    st.title("Image Flip App")

    # File uploader for selecting an image
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    # Check if an image file is selected
    if uploaded_file:
        try:
            # Display the uploaded image
            img = Image.open(uploaded_file)
            flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)

            # Use st.beta_columns to create two columns
            col1, col2 = st.columns(2)

            # Place each image in a separate column
            with col1:
                st.image(img, caption="Uploaded Image", use_column_width=True)

            with col2:
                st.image(flipped_img, caption="Flipped Image", use_column_width=True)

        # Generate a caption for the image (you can replace this with your captioning logic)
            # caption = generate_caption(uploaded_file.name)

            # Display the caption
            # st.write("Image Caption:")
            # st.write(caption)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please upload an image file.")


if __name__ == "__main__":
    main()