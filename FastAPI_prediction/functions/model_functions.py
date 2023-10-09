from sklearn.base import BaseEstimator, TransformerMixin
class ColumnDropper(BaseEstimator, TransformerMixin):
    def __init__(self, columns_to_drop):
        self.columns_to_drop = columns_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        if self.columns_to_drop is not None:
            return X.drop(self.columns_to_drop, axis=1,errors='ignore')
        else:
            return X