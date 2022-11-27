# Automatically train the model

## Introduction to Project Structure

![image-20221128005932233](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221128005932233.png)



## How to use

1. Just shoot a video around the desired gesture, then create a folder (one for each gesture) in the `GestureVideos` directory, and then put the corresponding video file into the corresponding folder. For example:

![image-20221127234028068](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221127234028068.png)

2. Run the main function, and you will get the trained model after the end. After the training, the test code will be run, and the predicted results and probabilities will be displayed in the window. The video is long and has many action angles, which can improve the accuracy of recognition.![image-20221127234422638](https://my-blogs-imgs-1312546167.cos.ap-nanjing.myqcloud.com//image-20221127234422638.png)

   You can get the corresponding gesture and model files in this way

   ```python
   ges= np.load(resource_path('DataForTraining/all_gestures.npy'),allow_pickle=True).tolist()
   
   model = load_model(resource_path('TrainingOutput/ModelFiles'))  # 加载训练好的tensorflow模型
   ```



Here is just an automatic training framework, you can replace it with what you want according to your own preferences.

## My Solution

1. Read the file location of the video, get the gestures that need to be trained and the location of the file
2. Call `mediapipe` to generate the training set in order by playing the pre-recorded video
3. Define the model, and then bring the training set generated by the video into the model for training
4. Save the model and test the running effect

## TODO

At present, this is a draft version that can be used but needs to be improved. Limited by the time and the level of the author, it has many places that can be optimized and upgraded.

- Use `numpy` arrays instead of `list` for better performance
- The part of generating the training set can increase the function of continuous training at breakpoints, which can be realized by recording the current training position
- The training part can add the functions of breakpoint training and `tensorboard` statistics
- You can use `PyQT5` to make the interface, which is more convenient for users to operate.
- The application of gesture recognition shortcut keys and the application of training can be integrated together
- could use a better model (hard)
- Operation support based on the result of two-hand recognition and controlling the mouse



## By the way 

The author is still a rookie in writing this project, and is currently preparing for the final exam and IELTS exam(It is so hard!). With my vocabulary, many sentences in the document cannot be expressed in English at all. Thanks to Google Translate, this project can have so many English words(Even these are mostly translated by Google Translate ) . During this period, some sentences may be confusing to read, which is probably because machine translation is not suitable for daily use in the past.
You are very welcome to point out the problems in the project or share the code for the project, I have a 50% probability that I can handle it well.





