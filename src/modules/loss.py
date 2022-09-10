import torch
import torch.nn as nn


class RMSELoss(nn.Module):
    """
    https://www.kaggle.com/code/yasufuminakama/fb3-deberta-v3-base-baseline-train#Loss
    """
    def __init__(self, reduction="mean", eps=1e-9):
        super().__init__()
        self.mse = nn.MSELoss(reduction="none")
        self.reduction = reduction
        self.eps = eps

    def forward(self, y_pred, y_true):
        loss = torch.sqrt(self.mse(y_pred, y_true) + self.eps)
        if self.reduction == "none":
            loss = loss
        elif self.reduction == "sum":
            loss = loss.sum()
        elif self.reduction == "mean":
            loss = loss.mean()
        return loss


if __name__ == "__main__":
    loss_fn = RMSELoss()

    y_pred = torch.rand(3)
    y_true = torch.rand(3)
    loss = loss_fn(y_pred, y_true)
