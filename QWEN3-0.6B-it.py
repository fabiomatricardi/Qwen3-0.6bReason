# Chat with an intelligent assistant in your terminal  with Falcon3-1B-Instruct.Q6_K.gguf
# model served in another terminal window with llama-server
from openai import OpenAI
import sys
from time import sleep
import rich
from rich.prompt import Confirm

STOPS = ['<|im_end|>']
COUNTERLIMITS = 10  #an even number

# ASCII ART FROM https://asciiart.club/
print("""

HI QWEN3
    
---
""")
# Point to the local server
client = OpenAI(base_url="http://localhost:8080/v1", api_key="not-needed")
print("3. Ready to Chat with Qwen3-0.6B  Context length=8192...")
print("\033[0m")  #reset all

history = [
]
print("\033[92;1m")
counter = 10
while True:
    if counter > COUNTERLIMITS:
        history = [
        ]        
    userinput = ""
    print("\033[1;30m")  #dark grey
    print("Enter your text (end input with Ctrl+D on Unix or Ctrl+Z on Windows) - type quit! to exit the chatroom:")
    print("\033[91;1m")  #red
    lines = sys.stdin.readlines()
    if "quit!" in lines[0].lower():
        print("\033[0mBYE BYE!")
        break    
    if Confirm.ask("Run [i]Thinking process[/i] ?", default=False):
        for line in lines:
            userinput += line + "/think \n"
    else:
        for line in lines:
            userinput += line + "/no_think \n"        

    history.append({"role": "user", "content": userinput})
    print("\033[92;1m")

    completion = client.chat.completions.create(
        model="local-model", # this field is currently unused
        messages=history,
        temperature=0.3,
        frequency_penalty  = 1.6,
        max_tokens = 1500,
        stream=True,
        stop=STOPS
    )

    new_message = {"role": "assistant", "content": ""}
    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content
    history.append(new_message)  
    counter += 1  



########################## MODEL CARD ###################################################
"""
#llama-server.exe -m Falcon3-1B-Instruct.Q6_K.gguf -c 8192 --port 8001
ggml_vulkan: Found 1 Vulkan devices:
ggml_vulkan: 0 = Intel(R) UHD Graphics (Intel Corporation) | uma: 1 | fp16: 1 | warp size: 32 | matrix cores: none
build: 4351 (4da69d1a) with MSVC 19.42.34435.0 for x64
system info: n_threads = 4, n_threads_batch = 4, total_threads = 4

system_info: n_threads = 4 (n_threads_batch = 4) / 4 | CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | AVX2 = 1 | F16C = 1 | FMA = 1 | LLAMAFILE = 1 | OPENMP = 1 | AARCH64_REPACK = 1 |

main: HTTP server is listening, hostname: 127.0.0.1, port: 8001, http threads: 3
main: loading model
srv    load_model: loading model 'Falcon3-1B-Instruct.Q6_K.gguf'
llama_load_model_from_file: using device Vulkan0 (Intel(R) UHD Graphics) - 8079 MiB free
llama_model_loader: loaded meta data with 38 key-value pairs and 165 tensors from Falcon3-1B-Instruct.Q6_K.gguf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
    general.architecture str              = llama
            general.name str              = Models Tiiuae Falcon3 1B Instruct
        general.finetune str              = Instruct
        general.basename str              = models-tiiuae-Falcon3
      general.size_label str              = 1.7B
         general.license str              = other
    general.license.name str              = falcon-llm-license
    general.license.link str              = https://falconllm.tii.ae/falcon-terms...
general.base_model.count u32              = 1
eneral.base_model.0.name str              = Falcon3 1B Base
ase_model.0.organization str              = Tiiuae
al.base_model.0.repo_url str              = https://huggingface.co/tiiuae/Falcon3...
            general.tags arr[str,1]       = ["falcon3"]
       general.languages arr[str,4]       = ["en", "fr", "es", "pt"]
        llama.vocab_size u32              = 131072
    llama.context_length u32              = 8192
  llama.embedding_length u32              = 2048
       llama.block_count u32              = 18
lama.feed_forward_length u32              = 8192
ama.rope.dimension_count u32              = 256
ama.attention.head_count u32              = 8
.attention.head_count_kv u32              = 4
n.layer_norm_rms_epsilon f32              = 0.000001
    llama.rope.freq_base f32              = 1000042.000000
       general.file_type u32              = 18
    tokenizer.ggml.model str              = gpt2
   tokenizer.ggml.tokens arr[str,131072]  = [">>TITLE<<", ">>ABSTRACT<<", ">>INTR...
   tokenizer.ggml.scores arr[f32,131072]  = [0.000000, 0.000000, 0.000000, 0.0000...
okenizer.ggml.token_type arr[i32,131072]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
   tokenizer.ggml.merges arr[str,128810]  = ["N E", "─á ─á", "─á t", "─á a", "> >...
enizer.ggml.eos_token_id u32              = 11
er.ggml.padding_token_id u32              = 2023
 tokenizer.chat_template str              = {% for message in messages %}{% if me...
ral.quantization_version u32              = 2
   quantize.imatrix.file str              = ./Falcon3-1B-Instruct-GGUF_imatrix.dat
quantize.imatrix.dataset str              = group_40.txt
ze.imatrix.entries_count i32              = 126
ize.imatrix.chunks_count i32              = 72
llama_model_loader: - type  f32:   37 tensors
llama_model_loader: - type q6_K:  128 tensors
llm_load_vocab: missing pre-tokenizer type, using: 'default'
llm_load_vocab:
llm_load_vocab: ************************************
llm_load_vocab: GENERATION QUALITY WILL BE DEGRADED!
llm_load_vocab: CONSIDER REGENERATING THE MODEL
llm_load_vocab: ************************************
llm_load_vocab:
llm_load_vocab: control-looking token:     11 '<|endoftext|>' was not control-type; this is probably a bug in the model. its type will be overridden
llm_load_vocab: special tokens cache size = 1
llm_load_vocab: token to piece cache size = 0.8741 MB
llm_load_print_meta: format           = GGUF V3 (latest)
llm_load_print_meta: arch             = llama
llm_load_print_meta: vocab type       = BPE
llm_load_print_meta: n_vocab          = 131072
llm_load_print_meta: n_merges         = 128810
llm_load_print_meta: vocab_only       = 0
llm_load_print_meta: n_ctx_train      = 8192
llm_load_print_meta: n_embd           = 2048
llm_load_print_meta: n_layer          = 18
llm_load_print_meta: n_head           = 8
llm_load_print_meta: n_head_kv        = 4
llm_load_print_meta: n_rot            = 256
llm_load_print_meta: n_swa            = 0
llm_load_print_meta: n_embd_head_k    = 256
llm_load_print_meta: n_embd_head_v    = 256
llm_load_print_meta: n_gqa            = 2
llm_load_print_meta: n_embd_k_gqa     = 1024
llm_load_print_meta: n_embd_v_gqa     = 1024
llm_load_print_meta: f_norm_eps       = 0.0e+00
llm_load_print_meta: f_norm_rms_eps   = 1.0e-06
llm_load_print_meta: f_clamp_kqv      = 0.0e+00
llm_load_print_meta: f_max_alibi_bias = 0.0e+00
llm_load_print_meta: f_logit_scale    = 0.0e+00
llm_load_print_meta: n_ff             = 8192
llm_load_print_meta: n_expert         = 0
llm_load_print_meta: n_expert_used    = 0
llm_load_print_meta: causal attn      = 1
llm_load_print_meta: pooling type     = 0
llm_load_print_meta: rope type        = 0
llm_load_print_meta: rope scaling     = linear
llm_load_print_meta: freq_base_train  = 1000042.0
llm_load_print_meta: freq_scale_train = 1
llm_load_print_meta: n_ctx_orig_yarn  = 8192
llm_load_print_meta: rope_finetuned   = unknown
llm_load_print_meta: ssm_d_conv       = 0
llm_load_print_meta: ssm_d_inner      = 0
llm_load_print_meta: ssm_d_state      = 0
llm_load_print_meta: ssm_dt_rank      = 0
llm_load_print_meta: ssm_dt_b_c_rms   = 0
llm_load_print_meta: model type       = ?B
llm_load_print_meta: model ftype      = Q6_K
llm_load_print_meta: model params     = 1.67 B
llm_load_print_meta: model size       = 1.28 GiB (6.56 BPW)
llm_load_print_meta: general.name     = Models Tiiuae Falcon3 1B Instruct
llm_load_print_meta: BOS token        = 11 '<|endoftext|>'
llm_load_print_meta: EOS token        = 11 '<|endoftext|>'
llm_load_print_meta: EOT token        = 11 '<|endoftext|>'
llm_load_print_meta: PAD token        = 2023 '<|pad|>'
llm_load_print_meta: LF token         = 2150 '├ä'
llm_load_print_meta: EOG token        = 11 '<|endoftext|>'
llm_load_print_meta: max token length = 256
ggml_vulkan: Compiling shaders..........................Done!
llm_load_tensors: offloading 0 repeating layers to GPU
llm_load_tensors: offloaded 0/19 layers to GPU
llm_load_tensors:   CPU_Mapped model buffer size =  1306.23 MiB
....................................................................
llama_new_context_with_model: n_seq_max     = 1
llama_new_context_with_model: n_ctx         = 8192
llama_new_context_with_model: n_ctx_per_seq = 8192
llama_new_context_with_model: n_batch       = 2048
llama_new_context_with_model: n_ubatch      = 512
llama_new_context_with_model: flash_attn    = 0
llama_new_context_with_model: freq_base     = 1000042.0
llama_new_context_with_model: freq_scale    = 1
llama_kv_cache_init:        CPU KV buffer size =   576.00 MiB
llama_new_context_with_model: KV self size  =  576.00 MiB, K (f16):  288.00 MiB, V (f16):  288.00 MiB
llama_new_context_with_model:        CPU  output buffer size =     0.50 MiB
llama_new_context_with_model:    Vulkan0 compute buffer size =   470.00 MiB
llama_new_context_with_model: Vulkan_Host compute buffer size =    20.01 MiB
llama_new_context_with_model: graph nodes  = 582
llama_new_context_with_model: graph splits = 202 (with bs=512), 1 (with bs=1)
common_init_from_params: setting dry_penalty_last_n to ctx_size = 8192
common_init_from_params: warming up the model with an empty run - please wait ... (--no-warmup to disable)
srv          init: initializing slots, n_slots = 1
slot         init: id  0 | task -1 | new slot n_ctx_slot = 8192
main: model loaded
main: The chat template that comes with this model is not yet supported, falling back to chatml. This may cause the model to output suboptimal responses
main: chat template, built_in: 0, chat_example: '<|im_start|>system
You are a helpful assistant<|im_end|>
<|im_start|>user
Hello<|im_end|>
<|im_start|>assistant
Hi there<|im_end|>
<|im_start|>user
How are you?<|im_end|>
<|im_start|>assistant
'
main: server is listening on http://127.0.0.1:8001 - starting the main loop
srv  update_slots: all slots are idle
"""
