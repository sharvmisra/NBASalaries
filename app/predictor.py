class NBASalaryPredictor:
    def __init__(self):
        # These coefficients are derived from our model
        self.intercept = -2661573.843363269
        self.coefficients = {
            'PTS': 734439.87545603,
            'TRB': 772734.98496597,
            'AST': 797461.91940453,
        }

    def predict_salary(self, PTS, TRB, AST):
        """
        Predicts the NBA player's salary based on points per game (PTS),
        total rebounds per game (TRB), and assists per game (AST).
        
        Parameters:
        - PTS: Points per game
        - TRB: Total rebounds per game
        - AST: Assists per game
        
        Returns:
        - Predicted salary
        """
        return (self.intercept +
                self.coefficients['PTS'] * PTS +
                self.coefficients['TRB'] * TRB +
                self.coefficients['AST'] * AST)

