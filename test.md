Input EEG Features (batch_size, 1, feature_dim)
                    ↓
┌─────────────────────────────────────────────────────────┐
│                Bidirectional LSTM                      │
│  ┌─────────────────┐    ┌─────────────────┐           │
│  │   Forward LSTM  │    │  Backward LSTM  │  Layer 1  │
│  │   (hidden_dim)  │    │   (hidden_dim)  │           │
│  └─────────────────┘    └─────────────────┘           │
│            ↓                      ↓                    │
│  ┌─────────────────┐    ┌─────────────────┐           │
│  │   Forward LSTM  │    │  Backward LSTM  │  Layer 2  │
│  │   (hidden_dim)  │    │   (hidden_dim)  │           │
│  └─────────────────┘    └─────────────────┘           │
└─────────────────────────────────────────────────────────┘
                    ↓
         Concatenated Output (hidden_dim * 2)
                    ↓
┌─────────────────────────────────────────────────────────┐
│              Multi-Head Attention                       │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐      │
│  │Head1│ │Head2│ │Head3│ │Head4│ │Head5│ │...8 │      │
│  └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘      │
└─────────────────────────────────────────────────────────┘
                    ↓
            Global Average Pooling
                    ↓
┌─────────────────────────────────────────────────────────┐
│                Enhanced Classifier                      │
│                                                         │
│  Linear(hidden_dim*2 → fc_hidden) → BatchNorm → ReLU   │
│                    ↓                                    │
│                Dropout(0.2)                            │
│                    ↓                                    │
│  Linear(fc_hidden → fc_hidden//2) → BatchNorm → ReLU   │
│                    ↓                                    │
│                Dropout(0.1)                            │
│                    ↓                                    │
│            Linear(fc_hidden//2 → 5)                    │
└─────────────────────────────────────────────────────────┘
                    ↓
        Sleep Stage Predictions (N1, N2, N3, REM, Wake)
