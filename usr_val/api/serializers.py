from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

from usr_val.utils import institute_email_validator, LowerEmailField, FileValidator
from usr_val.models import Teacher, Student, ResearchStatement


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    email = LowerEmailField(
        required=True,
        allow_blank=False,
        label='Email address',
        max_length=30,
        validators=[UniqueValidator(queryset=User.objects.all()), institute_email_validator],
    )
    first_name = serializers.CharField(
        required=True,
        max_length=60,
        allow_blank=False
    )
    last_name = serializers.CharField(
        required=False,
        max_length=60,
        allow_blank=True,
        default=''
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'confirm_password': 'Passwords must match'})
        account = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'].lower(),
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            is_active=False  # TO BE CHANGED TO FALSE
        )
        account.set_password(password)
        account.save()
        # send email from here
        return account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'groups', 'id']


class StudentRegistrationSerializer(serializers.ModelSerializer):
    avatar_thumbnail = serializers.ImageField(read_only=True)

    cv = serializers.FileField(allow_null=True,
                               max_length=100,
                               required=False,
                               use_url=True,
                               validators=[FileValidator(content_types=('application/pdf',), max_size=1024 * 1024)]
                               )
    dp = serializers.FileField(allow_null=True,
                               max_length=100,
                               required=False,
                               use_url=True,
                               validators=[FileValidator(content_types=('application/png',), max_size=1024 * 1024)]
                               )

    class Meta:
        model = Student
        exclude = ['user', ]


class CustomRSField(serializers.RelatedField):

    def to_representation(self, value):
        return value.research_statement


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    rs = CustomRSField(read_only=True)
    avatar_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'


class TeacherRegistrationSerializer(serializers.ModelSerializer):
    avatar_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Teacher
        exclude = ['user', ]


class TeacherSerializer(serializers.ModelSerializer):
    avatar_thumbnail = serializers.ImageField(read_only=True)

    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'


class RetrieveUpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', ]


class RetrieveUpdateStudentSerializer(serializers.ModelSerializer):
    avatar_thumbnail = serializers.ImageField(read_only=True)
    user = UserSerializer()

    class Meta:
        model = Student
        fields = '__all__'


class RetrieveUpdateTeacherSerializer(serializers.ModelSerializer):
    avatar_thumbnail = serializers.ImageField(read_only=True)

    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'


class RSSerializer(serializers.ModelSerializer):
    # student = StudentSerializer(read_only=True)

    class Meta:
        model = ResearchStatement
        exclude = ['student', ]


class RetrieveUpdateRSSerializer(serializers.ModelSerializer):
    # student = StudentSerializer()

    class Meta:
        model = ResearchStatement
        exclude = ['student', ]
