import os
import replicate
from openai import OpenAI
import openai

replicate_key = ""
deep_infra_key = ""
openai_key = ""

benchmark = [
    'ByteArray_Kotlin',
    'IllegalArgumentException_Kotlin',
    'BigDecimal_Kotlin',

    'GradientTape_TensorFlow',
    'Model_TensorFlow',
    'VariableSynchronization_TensorFlow',

    'MBeanServer_Java',
    'MessageDigest_Java',
    'UUID_Java',

    'Manifest_Android',
    'MediaPlayer_Android',
    'ActionBar_Android'
]

knowledge_type_descriptions = {
    "functionality": "describes the actions or operations an API can perform. For example, an functionality knowledge for tf.gather could be: 'tf.gather is used to select tensor elements at specific indices.'",
    "concept": "covers the foundational ideas and terminologies for understanding and effectively utilizing an API. For example, a concept knowledge for tf.gather could be: 'Tensor is essentially a high-dimensional array.'",
    "performance": "refers to the time and memory efficiency of an API. For example, a performance knowledge for tf.gather could be: 'tf.gather has overhead when used on large tensors.'",
    "directive": "is an essential type of knowledge that provides guidelines on the proper use of an API, including best practices to follow and actions to avoid. For example, a directive knowledge for tf.gather could be: 'When using tf.gather, ensure indices are within the shape of the input tensor.'",
    "pattern": "illustrates common use cases for applying the API to solve specific problems or achieve certain outcomes. For example, a pattern knowledge for tf.gather could be: 'tf.gather is commonly used in embedding lookup operations.'",
    "environment": "specifies the necessary conditions, system requirements, or configurations under which an API can function correctly. For example, an environment knowledge for tf.gather could be: 'tf.gather requires TensorFlow installed and supports both CPU and GPU execution.'",
    "alternative": "suggests other APIs offering similar functionality, which can be considered as replacements or complementary options. For example, an alternative knowledge for tf.gather could be: 'Alternatives to tf.gather include tf.scatter_nd and tf.index_select.'"
}

def gpt4(prompt):
    client = openai.OpenAI(
        api_key= openai_key,
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o",
    )
    return chat_completion.choices[0].message.content

def llama2_70b_chat(prompt):
    os.environ["REPLICATE_API_TOKEN"] = replicate_key
    api = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])
    output = api.run(
        "meta/llama-2-70b-chat",
            input={"prompt": prompt}
        )

    result = ""
    for item in output:
        result += item
        
    return result

def llama3_70b_instruct(prompt):
    os.environ["REPLICATE_API_TOKEN"] = replicate_key
    api = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])
    output = api.run(
        "meta/meta-llama-3-70b-instruct",
            input={"prompt": prompt}
        )

    result = ""
    for item in output:
        result += item
        
    return result

def mistral_7b_instruct_v3(prompt):
    openai = OpenAI(
        api_key=deep_infra_key,
        base_url="https://api.deepinfra.com/v1/openai",
    )

    chat_completion = openai.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.3",
        messages=[{"role": "user", "content": prompt}],
    )

    return chat_completion.choices[0].message.content