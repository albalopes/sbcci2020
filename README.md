In this work, one employ predictive models based on machine learning algorithms to enhance the design space exploration process of combining RAs and GPPs. Using this technique, we were able to achieve a prediction error rate above 2% and reduce the time for exploring the design space up to 104x when comparing with a scenario just using a high-level simulator tool.

For more details of our work, please consult our paper <b>"A Machine Learning Approach to Accelerating DSE of Reconfigurable Accelerator Systems"</b> at SBCCI 2020 Proceddings.

Check this project <a href="https://github.com/albalopes/sbcci2020/wiki/">Wiki</a> page for bechmark details, regression models descriptions and hyperparameters used in our experiments.

In this repository, we provide the subset of Mibench benchmarks used in our experiments; the databases we created to train the regression models; and the predicion outputs values after test the created regression models. The prediction values were used to calculate de Mean Absolute Error once Weka do not provide this metric as default.   
