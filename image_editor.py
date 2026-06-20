# Original Image
#      ↓
#  Grayscale
#      ↓
#    Blur
#      ↓
# Edge Detection
#      ↓
#    Save

import cv2

img = cv2.imread(r"C:\Users\fasna\OneDrive\Pictures\monkey.jpeg")

if img is None:
    print("No image found")
    exit()

edited_img = img.copy()

while True:

    print("\n----- IMAGE EDITOR -----")
    print("1. Grayscale")
    print("2. Resize")
    print("3. Blur")
    print("4. Edge Detection")
    print("5. Save Image")
    print("6. Show Current Image")
    print("7. Reset to Original")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        if len(edited_img.shape) == 3:
            edited_img = cv2.cvtColor(
                edited_img,
                cv2.COLOR_BGR2GRAY
            )

        cv2.imshow("Grayscale", edited_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == 2:

        width = int(input("Enter width: "))
        height = int(input("Enter height: "))

        edited_img = cv2.resize(
            edited_img,
            (width, height)
        )

        cv2.imshow("Resized", edited_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == 3:

        edited_img = cv2.GaussianBlur(
            edited_img,
            (5, 5),
            0
        )

        cv2.imshow("Blurred", edited_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == 4:

        if len(edited_img.shape) == 3:
            gray = cv2.cvtColor(
                edited_img,
                cv2.COLOR_BGR2GRAY
            )
        else:
            gray = edited_img

        edited_img = cv2.Canny(
            gray,
            100,
            200
        )

        cv2.imshow("Edges", edited_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == 5:

        filename = input("Enter filename: ")

        cv2.imwrite(
            filename + ".jpg",
            edited_img
        )

        print("Image saved successfully!")

    elif choice == 6:

        cv2.imshow(
            "Current Image",
            edited_img
        )

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == 7:

        edited_img = img.copy()

        print("Image reset to original.")

    elif choice == 8:

        print("Exiting...")
        break

    else:

        print("Invalid choice")