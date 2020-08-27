from setuptools import setup, find_packages

setup(
    name="kf-d3m-primitives",
    version="0.5.0",
    description="All Kung Fu D3M primitives as a single library",
    packages=find_packages(exclude="scripts"),
    setkeywords=['d3m_primitive'],
    install_requires=[
        "d3m",
        "tensorflow-gpu==2.2.0",
        "mxnet==1.6.0",
        "torch==1.4.0",
        "pillow==7.1.2",
        "tslearn",
        "statsmodels",
        "pmdarima>=1.6.1",
        "hdbscan",
        "requests",
        "shap>=0.35.0",
        "torchvision==0.5.0",
        "opencv-python-headless==4.1.1.26",
        "gluonts", 
        "albumentations",
        "tifffile",
        "punk @ git+https://github.com/uncharted-distil/punk@8b101eca26b5f9a3df2a65aab2733bd404965578#egg=punk",
        "object_detection_retinanet @ git+https://github.com/uncharted-distil/object-detection-retinanet@f4cba645c61a7bc068608356c6194adbe34f8e9e#egg=object_detection_retinanet",
        "Simon @ git+https://github.com/uncharted-distil/simon@00422bbdc9caa09b867f8b5f583487b59b605de0#egg=Simon",
        "nk_sent2vec @ git+https://github.com/uncharted-distil/nk-sent2vec@08a74ce1aff98e81eda2f3211ad7f7015bfa8124#egg=nk_sent2vec",
        "duke @ git+https://github.com/uncharted-distil/duke@c56416e959b52ff5077c5a54c329e2f6e83bbd97#egg=duke",
        "rsp @ git+https://github.com/cfld/rs_pretrained@92d832efe1961d6a06011f689dad7ef2481a64b1#egg=rsp"
    ],
    entry_points={
        "d3m.primitives": [
            "data_cleaning.column_type_profiler.Simon = kf_d3m_primitives.data_preprocessing.data_typing.simon:SimonPrimitive",
            "data_cleaning.geocoding.Goat_forward = kf_d3m_primitives.data_preprocessing.geocoding_forward.goat_forward:GoatForwardPrimitive",
            "data_cleaning.geocoding.Goat_reverse = kf_d3m_primitives.data_preprocessing.geocoding_reverse.goat_reverse:GoatReversePrimitive",
            "feature_extraction.nk_sent2vec.Sent2Vec = kf_d3m_primitives.natural_language_processing.sent2vec.sent2vec:Sent2VecPrimitive",
            "clustering.k_means.Sloth = kf_d3m_primitives.clustering.k_means.Storc:StorcPrimitive",
            "clustering.hdbscan.Hdbscan = kf_d3m_primitives.clustering.hdbscan.Hdbscan:HdbscanPrimitive",
            "clustering.spectral_graph.SpectralClustering = kf_d3m_primitives.clustering.spectral_clustering.spectral_clustering:SpectralClusteringPrimitive",
            "dimensionality_reduction.t_distributed_stochastic_neighbor_embedding.Tsne = kf_d3m_primitives.dimensionality_reduction.tsne.Tsne:TsnePrimitive",
            "time_series_classification.k_neighbors.Kanine = kf_d3m_primitives.ts_classification.knn.kanine:KaninePrimitive",
            "time_series_forecasting.vector_autoregression.VAR = kf_d3m_primitives.ts_forecasting.vector_autoregression.var:VarPrimitive",
            "time_series_classification.convolutional_neural_net.LSTM_FCN = kf_d3m_primitives.ts_classification.lstm_fcn.lstm_fcn:LstmFcnPrimitive",
            "time_series_forecasting.lstm.DeepAR = kf_d3m_primitives.ts_forecasting.deep_ar.deepar:DeepArPrimitive",
            "object_detection.retina_net.ObjectDetectionRN = kf_d3m_primitives.object_detection.retinanet.object_detection_retinanet:ObjectDetectionRNPrimitive",
            "data_cleaning.data_cleaning.Datacleaning = kf_d3m_primitives.data_preprocessing.data_cleaning.data_cleaning:DataCleaningPrimitive",
            "data_cleaning.text_summarization.Duke = kf_d3m_primitives.data_preprocessing.text_summarization.duke:DukePrimitive",
            "feature_selection.pca_features.Pcafeatures = kf_d3m_primitives.feature_selection.pca_features.pca_features:PcaFeaturesPrimitive",
            "feature_selection.rffeatures.Rffeatures = kf_d3m_primitives.feature_selection.rf_features.rf_features:RfFeaturesPrimitive",
            "classification.inceptionV3_image_feature.Gator = kf_d3m_primitives.image_classification.imagenet_transfer_learning.gator:GatorPrimitive",
            "remote_sensing.remote_sensing_pretrained.RemoteSensingPretrained = kf_d3m_primitives.remote_sensing.featurizer.remote_sensing_pretrained:RemoteSensingPretrainedPrimitive",
            "remote_sensing.mlp.MlpClassifier = kf_d3m_primitives.remote_sensing.classifier.mlp_classifier:MlpClassifierPrimitive",
        ],
    },
)
