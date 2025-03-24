# **GenAI Security Manager - Must to Have Features**

## **Purpose, Scope and Background**

This guide describes the steps required to use the GenAI Security Manager Application and create BigQuery Row Level Security Policy.

**IMPORTANT:**

**This application is a prototype and should be used for experimental purposes only. It is not intended for production use. This software is provided 'as is' without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall Google or the developers be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software. Google is not responsible for the functionality, reliability, or security of this prototype. Use of this tool is at your own discretion and risk.**

## **Features to be implemented by the customers/partners**

This ia a list of a features to be implemented by the customer/partner to be a MVP:

* **Audit Log**
    * Track all user action on the application and all changes/updates on policies, like: insert values on policy, creating a policy, deleting a policy and etc. 

* **Authentication Integration**
    * Integration of User Authentication on application login using GCP User to run all commands. Eg: When user create a policy, use the user credentials to create it.

* **Roles and Permission Mechanism**
    * Develop a roles/permission mechanism inside de application. Eg: A user can only assign values to the policy and not create a policy.

