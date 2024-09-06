from django.urls import path
from .views import HomeView, UserCreateView, VerifyOtpView, RegenerateOtpView, ForgotPasswordView, VerifyForgotOtpView, LogoutView, ValidateTokenView, ChangePasswordView, AdminLoginView


urlpatterns = [
    path("signup", UserCreateView.as_view(), name="User Create"),
    path("verify-otp", VerifyOtpView.as_view(), name="VerifyOtp"),
    path("resend-otp", RegenerateOtpView.as_view(), name="RegenerateOtp"),
    path("forgot-password", ForgotPasswordView.as_view(), name="ForgotPassword"),
    path("verify-forgot-otp", VerifyForgotOtpView.as_view(), name="VerifyForgotOtp"),
    path("change-password", ChangePasswordView.as_view(), name="ChangePassword"),
    # path("jobseeker-login", JobSeekerLoginView.as_view(), name="Employee Login"),
    # path("employer-login", EmployerLoginView.as_view(), name="Employer Login"),
    path("admin-login", AdminLoginView.as_view(), name="Admin Login"),
    path("logout", LogoutView.as_view(), name="Logout"),
    path("validate-token", ValidateTokenView.as_view(), name="ValidateToken"),


]