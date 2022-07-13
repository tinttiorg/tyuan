Object Tracking
===============



We mainly put our emphasis on autonomtive object tracking, especially the extended object tracking. 


Tracker uses mainly three elementary knowledge:

- noise model: uncertainties.
- system dynamics: state evolution and prior information,
- measurement system: sensor,


to extract two essential information:

- quality, i.e., accuracy and reliability, higher than the raw measurements
- inference information, not directly available in the measurements.

For serious Bayesian researchers, it is highly recommended to read [#]_:

1. :`Purple Bible`_: Estimation with Applications to Tracking and Navigation by Yaakov Bar-Shalom, X. Rong Li and Thiagalingam Kirubarajan.

2. :`Yellow Brick`_: Tracking and Data Fusion: A Handbook of Algorithms by Yaakov Bar-Shalom, Peter K. Willett and Xin Tian.

3. :`Grey Manual`_: Design and Analysis of Modern Tracking Systems (Artech House Radar Library) by Samuel Blackman and Robert Popoli.  


.. admonition:: Stone Soup by DSTL 


	A wonderful **point target** tutorial for industrial engineers is presented by the Defence Science and Technology Laboratory (DSTL), called `Stone Soup`_. 

	Stone Soup is developed in Python with six major components: framework, data, algorithms, metrics, simulators, and sensor models. The framework is the core of the project and as a software architecture in a modular fashion integrating all essence in Tracking (such as dynamic/measurement models, noise metrics and simulators).

    .. figure:: image/figSSframework.jpg
        :align: center
        :alt: Stone Soup Structure

        Fig. 01: Stone Soup Structure    



One of our major efforts is to design an Extended Object Tracking Framework similar to the `Stone Soup`_. 

However, before applying the tracking/estimation theory originated from aerospace systems for automotive applications, we must understand their common ground and differences.

.. admonition:: Automotive Tracking versus Aerospace Tracking  

    .. csv-table:: 

   		**Automotive**, **Aerospace**
        weak Gaussian assumption, strong Gaussian assumption 
        extended object, point target
        kinematic and shape association, probablistic association


Let us call the system **OCEAN**.

.. admonition:: Ocean by UniverSee

	The **Ocean** consists mainly of the following modules:

	1. Framework for extended object tracking (EOT)
	2. Dynamic model set
	3. Measurement model set
	4. Mutltiple model toolbox
	5. Association scheme
	6. Performance metrics
	7. Pre-Processing tool















---------------------------------------------------------------------------------------------------

.. [#] mentioning my name, you might get some discount, :-)





.. _Purple Bible: https://www.amazon.com/Estimation-Applications-Tracking-Navigation-Bar-Shalom/dp/047141655X
.. _Yellow Brick: https://www.amazon.com/Tracking-Data-Fusion-Handbook-Algorithms/dp/0964831279
.. _Grey Manual: https://www.amazon.com/Design-Analysis-Tracking-Systems-Library/dp/1580530060/ref=pd_lpo_1?pd_rd_i=1580530060&psc=1
.. _Stone Soup: https://stonesoup.readthedocs.io/



