from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  UniqueConstraint

db = SQLAlchemy()

class RepoAnalyzeResult(db.Model):
    __tablename__ = 'repo_analyze_result'  # 確保表名與數據庫中實際創建的表名一致


    def __repr__(self):
        return f"<Result {self.repo_url} - {self.file} - {self.criterion}: {self.score} (commit: {self.commit})>"

class AverageScore(db.Model):
    __tablename__ = 'average_scores'

    commit = db.Column(db.String, index=True)

    # 定義關聯 待完善
    # repo_analyze_results = db.relationship('RepoAnalyzeResult', backref='average_scores', lazy=True)

    def __repr__(self):
        return f"<AverageScore {self.repo_url} - {self.file} - {self.criterion}: {self.average_score} (commit: {self.commit})>"
