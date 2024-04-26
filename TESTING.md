# Mildew Detector - Testing

## Testing

Testing was conducted at several stages throughout the development on both Streamlit being run from the workspace and later the deployed app on Heroku. 

## Full Manual Testing

### Project Overview Page

**Feature/Function**|**Expected Outcome**|**Method of Test**|**Result**|**Pass/Fail**
:-----:|:-----:|:-----:|:-----:|:-----:
Navigation option for Project Overview Page|Stays on Project Overview Page|Clicked Project Overview Page radio button option|Stayed on Project Overview Page|Pass
Navigation option for Leaf Visualiser Page|Redirects to Leaf Visualisation page|Clicked Leaf Visualisation radio button option|Redirected to Leaf Visualisation page|Pass
Navigation option for Mildew Detector Page|Redirects to Mildew Detector page|Clicked Mildew Detector radio button option|Redirected to Mildew Detector page|Pass
Navigation option for ML Performance Page|Redirects to ML Performance Page|Clicked ML Performance radio button option|Redirected to ML Performance page|Pass
Navigation option for Project Hypotheses Page|Redirects to Project Hypotheses page|Clicked show Project Hypotheses page button|Project Hypotheses page shown|Pass
Show Project Hypotheses and Validation Criteria Box|Shows project hypotheses and validation criteria|Clicked Show project hypotheses and validation criteria button|Project hypotheses and validation criteria shown|Pass

### Leaves Visualiser Page

**Feature/Function**|**Expected Outcome**|**Method of Test**|**Result**|**Pass/Fail**
:-----:|:-----:|:-----:|:-----:|:-----:
Navigation option for Project Overview Page|Redirects to Project Overview Page|Clicked Project Overview radio button option|Redirected to Project Overview Page|Pass
Navigation option for Leaf Visualiser Page|Remain on Leaf Visualisation page|Clicked Leaf Visualisation radio button option|Remained on Leaf Visualisation page|Pass
Navigation option for Mildew Detector Page|Redirects to Mildew Detector page|Clicked Mildew Detector radio button option|Redirected to Mildew Detector page|Pass
Navigation option for Project Hypotheses Page|Redirects to Project Hypothese page|Clicked Project Hypothese radio button option|Redirected to Project Hypothese page|Pass
Show Difference between and Average Variablility Button|Shows the saved images of the average and variability of healthy and powdery mildew leaves |Clicked the Show Difference between and Average Variablility Button|The saved images of the average and variability of healthy and powdery mildew leaves shown|Pass
Show chart for difference between healthy and powdery mildew leaves button|Shows saved images of differences between average healthy and powdery mildew leaves|Clicked show chart for differences button|Images of differences between average healthy and powdery mildew leaves shown|Pass
Show Image Montage|A selection of saved images from the data are displayed|Clicked the show image montage button|A selection of saved images from the data were displayed|Pass

### Mildew Detector Page

**Feature/Function**|**Expected Outcome**|**Method of Test**|**Result**|**Pass/Fail**
:-----:|:-----:|:-----:|:-----:|:-----:
Navigation option for Project Overview Page|Redirects to Project Overview Page|Clicked Project Overview radio button option|Redirected to Project Overview Page|Pass
Navigation option for Leaf Visualiser Page|Redirects to Leaf Visualisation page|Clicked Leaf Visualisation radio button option|Redirected to Leaf Visualisation page|Pass
Navigation option for Mildew Detector Page|Remains to Mildew Detector page|Clicked Mildew Detector radio button option|Remained to Mildew Detector page|Pass
Navigation option for Project Hypotheses Page|Redirects to Project Hypothese page|Clicked Project Hypothese radio button option|Redirected to Project Hypothese page|Pass
Upload Image Option with .png image|Prediction is made with figures and details shown|Uploaded .png image|Prediction was made with figures and details shown|Pass
Upload Image with non .png image|Error message explaining only .png formats can be accepted shown|Uploaded non .png image|Error message explaining only .png formats can be accepted shown|Pass
Healthy leaf .png prediction|Prediction of uninfected is displayed|Uploaded health leaf .png image|Prediction of uninfected was displayed|Pass
Healthy leaf .png prediction probability figure|Figure showing prediction probability in green bar graph displayed|Upload healthy leaf .png image|Figure showing prediction probability in green bar graph displayed|Pas
Powdery mildew leaf .png prediction|Prediction of infected is displayed|Upload image of leaf infected with powdery mildew in .png format|Prediction of infected is displayed|Pass
Powdery mildew prediction probability figure|Figure showing prediction probability in red bar graph displayed|Upload image of leaf infected with powdery mildew in .png format|Figure showing prediction probability in green red graph displayed|Pass
Download Prediction Report|Downloads an excel file containing the predicitons on uploaded image(s)|Clicked download report button after uploading image|Excel file downloaded which contains the predictions and details of the image files uploaded|Pass

### Project Hypotheses and Validation Page

**Feature/Function**|**Expected Outcome**|**Method of Test**|**Result**|**Pass/Fail**
:-----:|:-----:|:-----:|:-----:|:-----:
Navigation option for Project Overview Page|Redirects to Project Overview Page|Clicked Project Overview radio button option|Redirected to Project Overview Page|Pass
Navigation option for Leaf Visualiser Page|Redirects to Leaf Visualisation page|Clicked Leaf Visualisation radio button option|Redirected to Leaf Visualisation page|Pass
Navigation option for Mildew Detector Page|Redirects to Mildew Detector page|Clicked Mildew Detector radio button option|Redirected to Mildew Detector page|Pass
Navigation option for Project Hypotheses Page|Remains to Project Hypothese page|Clicked Project Hypothese radio button option|Remained to Project Hypothese page|Pass
