# noopy-sample
Usage of noopy(https://github.com/acuros/noopy)

## How to use
1. Before you start, you have to create appropriate role for your lambda function. In this sample, we use [role with this policy](./sample_exec_role_policy.json) (Learn more in [here](https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html#lambda-intro-execution-role))
2. And then, you have to grant permissions to your iam account to create Lambda function, pass role created in step 1, create API Gateway rest api. In this sample, we use both [this](./sample_user_policy1.json) and [this](./sample_user_policy2.json)
3. Start project with ``noopy-admin startproject <project name>``. You have to input your information.

  ```
  $noopy-admin startproject sample
  Input aws account id > 123456789012
  Input role arn to be granted to lambda function > arn:aws:iam::123456789012:role/lambda_basic_execution
  Project "test123" created
  ```
  
4. Edit [views](./src/views.py) as you want
5. Deploy it

  ```
  $python deploy.py
  https://qpf9qhl0jk.execute-api.ap-northeast-1.amazonaws.com/prod
  ```
  
