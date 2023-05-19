# TV-Test-Driver
  This program consist of a class named TV and a Test driver which is a separate python file. Using the Class named TV, two objects, namely Television 1 and Television 2, is created. These objects will perform functions of Class TV and create an output status of both television shown on the following:
  ```
  Output:
  Television 1's channel is 'int'. The volume level of Television 1 is 'int'.
  Television 2's channel is 'int'. The volume level of Television 2 is 'int'. 
  ```

***
  # Flow
  
  1. The class will be performed on a Test Driver where objects were created.
  2. The program will start from Object 1.
  3. The User will be asked to Turn the Television 'On' or 'Off'.
      + If the Television is 'On', the status will be printed on the outline.
      + If the Television is 'Off', the user will be advised that the Television is off on the output.
   4. The program will ask for the desired channel. (Choose from 1 to 120 only)
   5. The program will ask if the user wanted to change the channel. It is answerable by 'yes' or 'no' only.
      + If yes, program will allow the user to enter the new channel. Then, it will ask the same questions until the user responded 'no' when asked to change the channel.
      + If no, the program will proceed.
   6. The program will be asked for the desired volume level. (Choose from 1 to 7 only)
   7. The program will ask if the the user wanted to change the volume level. It is answerable by 'yes' or 'no' only.
      + If yes, program will allow the user to enter the new volume level. Then, it will ask the same questions until the user responded 'no' when asked to change the channel.
      + If no, the program will proceed.
   8.  The user will be asked to increase the Channel by one. It is answerable by 'yes' or 'no' only.
      + This function will be repeated as long as the user response is 'yes'
   9.  The user will be asked to decrease the Channel by one. It is answerable by 'yes' or 'no' only.
      + This function will be repeated as long as the user response is 'yes'
   10.  The user will be asked to increase the volume by one. It is answerable by 'yes' or 'no' only.
      + This function will be repeated as long as the user response is 'yes'
   11.  The user will be asked to decrease the volume by one. It is answerable by 'yes' or 'no' only.
      + This function will be repeated as long as the user response is 'yes'
   12.  The final status of Television will be shown as below:
   ```
   Channel: int
   Volume Level: int
   Power On?: Bool
   ```
   13. The process will be repeated from step 2. However, it will be under object 2 or Television 2.
   14. Lastly, the program will show the status of both objects along with their final channel and final volume level.


***

  
