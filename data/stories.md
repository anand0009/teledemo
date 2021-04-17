## happy path greet 
* greet
  - utter_greet
* chit_chat
   - utter_default

## chitchat
* chit_chat
   - utter_default 
* thanks
  - utter_goodbye

## say goodbye
* greet
  - utter_greet
* chit_chat
   - utter_default 
* goodbye
  - utter_goodbye

## bot challenge
* chit_chat
   - utter_default 
* bot_challenge
  - utter_iamabot
* goodbye
  - utter_goodbye

## chit chat 
* chit_chat
   - utter_default

## New Story

* greet
    - utter_greet
* bot_challenge
    - utter_iamabot
* greet
    - utter_greet
* chit_chat
    - utter_default

## New Story
* greet
    - utter_greet
* thanks
    - utter_goodbye

## New Story

* greet
    - utter_greet
* new_plan
    - action_new_plan

## New Story

* greet
    - utter_greet
* greet
    - utter_greet
* new_plan
    - action_new_plan
* thanks
    - utter_welcome

## get my plan
* greet
    - utter_greet
* my_plan
    -  utter_your_num
* user_phone_number{"PHONE_NUMBER":"8921249971"}
    -  slot{"PHONE_NUMBER":"8921249971"}
    - action_your_plan
* thanks
    - utter_welcome

## New Story

* greet
    - utter_greet
* new_plan
    - action_new_plan
* greet
    - utter_greet
* new_plan
    - action_new_plan
* thanks
    - utter_welcome
* greet
    - utter_greet
* my_plan
    - utter_your_num
* user_phone_number{"PHONE_NUMBER":"8921249971"}
    - slot{"PHONE_NUMBER":"8921249971"}
    - action_your_plan

## New Story

* greet
    - utter_greet
* my_plan
    - utter_your_num
* user_phone_number{"PHONE_NUMBER":"8921249971"}
    - slot{"PHONE_NUMBER":"8921249971"}
    - action_your_plan
* thanks
    - utter_welcome
* bot_challenge
    - utter_iamabot
* new_plan
    - action_new_plan
* thanks
    - utter_goodbye
* goodbye
    - utter_goodbye

## New Story

* greet
    - utter_greet
* my_plan
    - utter_your_num
* user_phone_number{"PHONE_NUMBER":"8921249971"}
    - slot{"PHONE_NUMBER":"8921249971"}
    - action_your_plan
* thanks
    - utter_welcome
* new_plan
    - action_new_plan
* affirm
    - utter_default

## New Story

* greet
    - utter_greet
* network_issue
    - utter_tell_issue
* facing_issue
    - utter_what_handset
* headset{"BRAND":"samsung"}
    - slot{"BRAND":"samsung"}
    - utter_change_settings
* guide_me
    - utter_solution
* have_to_do
    - utter_solution_4G
* thanks
    - utter_welcome

## New Story

* greet
    - utter_greet

* facing_issue
    - utter_what_handset
* headset
    - utter_change_settings
* guide_me
    - utter_solution
* have_to_do
    - utter_solution_4G
 * thanks
    - utter_welcome
## story my plan
* greet
    - utter_greet
* my_plan
    -  utter_your_num
* user_phone_number{"PHONE_NUMBER":"8921249971"}
    -  slot{"PHONE_NUMBER":"8921249971"}
    - action_your_plan
* thanks
    - utter_welcome