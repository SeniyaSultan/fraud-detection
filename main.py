from src.data_preprocessing import load_data, preprocess
from src.eda import plot_histogram, plot_bivariate, correlation_heatmap
from src.modeling import split_and_resample, train_model, evaluate_model

df = load_data('data/fraud_data.csv')
if df is not None:
    df = preprocess(df)
    plot_histogram(df, 'amount')
    plot_bivariate(df, 'is_fraud', 'amount')
    correlation_heatmap(df)

    X = df.drop('is_fraud', axis=1)
    y = df['is_fraud']
    X_train, X_test, y_train, y_test = split_and_resample(X, y)

    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
