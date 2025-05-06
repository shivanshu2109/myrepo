graph TD
    %% Main Model Types
    TextModel["Text-Only Model"]
    ImageModel["Image-Only Model"]
    FusionModel["Fusion Model"]
    
    %% Text Model Architecture
    TextModel --> TextInput["Plot Synopsis Input"]
    TextInput --> Tokenization["Tokenization<br>DistilBertTokenizerFast<br>256 tokens, truncation, padding"]
    Tokenization --> DistilBERT["DistilBERT Base<br>distilbert-base-uncased"]
    DistilBERT --> TextFC["Fully Connected Layers<br>with Dropout"]
    TextFC --> TextSigmoid["Sigmoid Activation"]
    TextSigmoid --> TextOutput["Genre Predictions"]
    
    %% Text Model Training
    TextModel --> TextTraining["Training"]
    TextTraining --> TextLoss["BCEWithLogitsLoss"]
    TextTraining --> TextOptimizer["AdamW<br>LR: 2e#45;5"]
    TextTraining --> TextTechniques["Mixed#45;precision<br>Gradient clipping<br>Early stopping on F1"]
    
    %% Image Model Architecture
    ImageModel --> ImageInput["Poster Image Input"]
    ImageInput --> ImagePreprocess["Preprocessing<br>Resize to 224x224<br>ImageNet normalization<br>Random horizontal flip"]
    ImagePreprocess --> ConvNeXt["ConvNeXt#45;Tiny<br>ImageNet pre#45;trained"]
    ConvNeXt --> ImageHead["Linear → ReLU → Dropout → Linear"]
    ImageHead --> ImageSigmoid["Sigmoid Activation"]
    ImageSigmoid --> ImageOutput["Genre Predictions"]
    
    %% Image Model Training
    ImageModel --> ImageTraining["Training"]
    ImageTraining --> ImageLoss["BCEWithLogitsLoss"]
    ImageTraining --> ImageOptimizer["AdamW<br>LR: 1e#45;4"]
    ImageTraining --> ImageTechniques["Mixed#45;precision<br>GradScaler<br>Selective backbone fine#45;tuning"]
    
    %% Fusion Model Architecture
    FusionModel --> FusionTextInput["Plot Synopsis Input"]
    FusionModel --> FusionImageInput["Poster Image Input"]
    FusionTextInput --> FusionTokenization["Text Processing"]
    FusionTokenization --> FusionDistilBERT["DistilBERT<br>[CLS] token"]
    FusionImageInput --> FusionImagePreprocess["Image Processing"]
    FusionImagePreprocess --> FusionConvNeXt["ConvNeXt#45;Tiny<br>pooled feature"]
    FusionDistilBERT --> FeatureConcatenation["Feature Concatenation"]
    FusionConvNeXt --> FeatureConcatenation
    FeatureConcatenation --> FusionFC["Fully Connected Layers"]
    FusionFC --> FusionSigmoid["Sigmoid Activation"]
    FusionSigmoid --> FusionOutput["Genre Predictions"]
    
    %% Fusion Model Training
    FusionModel --> FusionTraining["Training"]
    FusionTraining --> FusionLoss["BCEWithLogitsLoss"]
    FusionTraining --> FusionOptimizer["AdamW"]
    FusionTraining --> FusionTechniques["Mixed#45;precision<br>GradScaler<br>Flexible encoder freezing<br>Batch size: 192<br>Gradient accumulation<br>Early stopping on macro F1"]
    
    %% Styling
    classDef modelTitle fill:#f9f,stroke:#333,stroke-width:2px;
    class TextModel,ImageModel,FusionModel modelTitle;
