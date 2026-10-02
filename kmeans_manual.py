"""K-Means from scratch — Lab 05.

Hoàn thiện các TODO. Không dùng sklearn trong file này.
Chỉ dùng NumPy.
"""

import numpy as np


def init_centroids(X, k, random_state=42):
    """Chọn ngẫu nhiên k điểm khác nhau trong X làm centroid ban đầu.

    Parameters
    ----------
    X : array-like, shape (n_samples, n_features)
    k : int
    random_state : int

    Returns
    -------
    centroids : ndarray, shape (k, n_features)
    """
    # TODO
    raise NotImplementedError


def assign_clusters(X, centroids):
    """Gán mỗi điểm vào centroid gần nhất theo Euclidean distance.

    Returns
    -------
    labels : ndarray, shape (n_samples,)
    """
    # TODO
    raise NotImplementedError


def update_centroids(X, labels, old_centroids):
    """Tính centroid mới bằng trung bình các điểm trong từng cụm.

    Nếu một cụm rỗng, giữ nguyên centroid cũ của cụm đó.
    """
    # TODO
    raise NotImplementedError


def kmeans_manual(X, k, max_iters=100, tol=1e-4, random_state=42):
    """Chạy K-Means cho tới khi centroid gần như không đổi.

    Dùng np.allclose(..., atol=tol) để kiểm tra hội tụ.

    Returns
    -------
    centroids : ndarray
    labels : ndarray
    n_iters : int
    """
    # TODO
    raise NotImplementedError
