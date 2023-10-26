In their study, the authors of the **tomatOD** focus on selective cropping and treatment tasks where learning algorithms can enhance crop growth and disease prediction, species recognition, and fruit detection. They introduce a specialized dataset for tomato fruit object detection and classification. This dataset consists of 277 images with 2418 annotated tomatoes and contains information about the ripening stage (unripe, semi-ripe, and fully ripe) of each tomato fruit along with its corresponding bounding box. Its purpose is to encourage the development of task-specific object detection algorithms for production-ready applications and to serve as a baseline for common state-of-the-art object detection algorithms. 

The tomatOD dataset is a novel collection created to simulate the scenario of a robotic arm navigating a soilless tomato cultivation greenhouse, mapping locations and estimating the ripening stages of each tomato fruit. The authors conducted data acquisition in a controlled environment, capturing images of tomato plants with varying ripening stages. The annotations were made manually by expert agriculturists, ensuring the accuracy of the training data for detection algorithms. The dataset's statistical analysis reveals insights into the dataset's content, including the relative size distribution (%) of bounding boxes, the number of labelled instances per image, and the number of categories in images. 

<p float="left">
  <img src="https://github.com/supervisely/dataset-tools/assets/78355358/26df1971-6374-49e5-ba3c-5405757078ba" width="30%" />
  <img src="https://github.com/supervisely/dataset-tools/assets/78355358/b9726922-b1da-44fe-aa20-0a9fd319c991" width="30%" /> 
  <img src="https://github.com/supervisely/dataset-tools/assets/78355358/6f6023d5-9d3f-4a0f-8af2-2950797edbe7" width="30%" /> 
</p>

Additionally, the authors propose an official 80%/20% *train*-*test* split for the dataset, ensuring that algorithms evaluated on it can provide easily comparable results. This split was determined using a semi-random approach, taking into account the dataset's characteristics.

Overall, the TomatOD dataset serves as a valuable resource for developing and testing object detection algorithms tailored for tomato fruit detection and classification in the context of precision farming.
