"""
-- Created by: Ashok Kumar Pant
-- Email: asokpant@gmail.com
-- Created on: 04/05/2025
"""
from cacs456ml.entity.common import ErrorCode
from cacs456ml.entity.recommendation import Recommendation
from cacs456ml.entity.recommendation_reqres import GetRecommendationRequest, GetRecommendationResponse
from cacs456ml.util import strutil


class RecommendationService:
    def __init__(self):
        pass

    def get_recommendations(self, req: GetRecommendationRequest) -> GetRecommendationResponse:
        if strutil.is_empty(req.user_id):
            return GetRecommendationResponse(error=True, error_code=ErrorCode.BAD_REQUEST, message="Invalid input")

        recommendations = []
        recommendations.append(
            Recommendation(
                user_id=req.user_id,
                item_id="1",
                score=0.9,
            ))
        recommendations.append(
            Recommendation(
                user_id=req.user_id,
                item_id="2",
                score=0.8,
            ))
        res = GetRecommendationResponse(
            error=False,
            recommendations=recommendations
        )
        return res
