import streamlit as st
import re
import base64

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Flo Email Footer Generator", page_icon="📧")

st.title("📧 Flo Mattress — Email Footer Generator")
st.markdown("Fill in your details below to generate your personalised email footer.")
st.divider()

# ── HTML template (the footer) ────────────────────────────────────────────────
HTML_TEMPLATE = """<!DOCTYPE html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Flo Mattress E-Signature #18</title>

    <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Poppins:100,200,400,500,600,700,800,900" />

    <style type="text/css">

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500&display=swap');

    * {
        font-family: 'Poppins', sans-serif !important;
    }

    /* Client-Specific styles */
    #outlook a { padding:0; }
    body { width:100% !important; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%; margin:0; padding:0; border:0; }

    .ExternalClass 	{ width:100%; }
    .ExternalClass,
    .ExternalClass p,
    .ExternalClass span,
    .ExternalClass font,
    .ExternalClass td,
    .ExternalClass div { line-height:100%; }
    img { outline:none; text-decoration:none;border:none; -ms-interpolation-mode:bicubic; }
    a img { border:none; text-decoration:none;border:none; -ms-interpolation-mode:bicubic; }
    p { margin:0px 0px !important; }
    table { border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt; }
    table td { border-collapse:collapse; }

    @media only screen and (max-width: 640px) {
        a[href^="tel"], a[href^="sms"] {
            text-decoration:none;
            color:#000000;
            pointer-events:none;
            cursor:default;
        }
        .mobile_link a[href^="tel"], .mobile_link a[href^="sms"] {
            text-decoration:default;
            color:#000000 !important;
            pointer-events:auto;
            cursor:default;
        }
    }

    @media only screen and (max-width: 480px) {
        a[href^="tel"], a[href^="sms"] {
            text-decoration:none;
            color:#000000;
            pointer-events:none;
            cursor:default;
        }
        .mobile_link a[href^="tel"], .mobile_link a[href^="sms"] {
            text-decoration:default;
            color:#000000 !important;
            pointer-events:auto;
            cursor:default;
        }
    }

.autoheight{
    height: 40px;
}

.autoheight2{
    height: 45px;
}

.autocenter{
    text-align: center;
}
    @media only screen and (max-width: 480px) {
        td[class=wrapper] {
            padding-top:0 !important;
            padding-left:0 !important;
            padding-right:0 !important;
        }

        table[class=mobile-view], td[class=mobile-view], img[class=mobile-view] {
            width:320px !important;
            height:auto !important;
        }

        td[class=clump] {
            display:block !important;
            padding-left:0 !important;
            padding-right:0 !important;
            width:100% !important;
        }

        td[class=aligncenter] {
            width:300px !important;
            height:auto !important;
            text-align:center !important;
        }
    }
</style>
</head>

<body>

    <table width="800" border="0" cellspacing="0" cellpadding="0" class="mobile-view" style="border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;">
        <tbody>
            <tr>
                <td width="90" valign="top" align="left" style="padding:0 10px 20px 0;" class="clump">
                    <table width="90" border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;">
                        <tr>
                            <td valign="middle" align="center" style="width:90px; height:auto; background:#ffffff; padding:5px 0;">
                                <img src="https://res.cloudinary.com/dyvpxfltr/image/upload/f_auto,q_auto/logo_vbvhpp" alt="Flo Mattress" width="90" border="0" style="display:block; border:0; outline:none;" />
                            </td>
                        </tr>
                    </table>
                </td>
                <td valign="top" align="left" style="padding:0 0 20px 0;" class="clump">
                    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;">
                        <tbody>
                            <tr>
                                <td colspan="4" style="padding:0 0 0 10px;">
                                    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;">
                                        <tr>
                                            <td style="font-family:'Poppins', sans-serif, Arial; font-size:18px; line-height:24px; text-transform:none; font-weight:400; color:#2f3542;text-transform: capitalize;">Tanmay Badgujar</td>
                                        </tr>
                                        <tr>
                                            <td style="font-family:'Poppins', sans-serif, Arial; font-size:11px; line-height:18px; font-weight:400; color:#a3a7b2;">Executive Data Analyst</td>
                                        </tr>
                                        <tr>
                                            <td style="padding:15px 0 10px 0;"><img src="https://smsquotes.org/emailimages/divider.png" alt="divider" width="30" height="1" border="0" style="display:block; outline:none; border:0;" /></td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>

                            <tr>
                                <td colspan="4" style="padding:0 0 15px 10px;">
                                    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;">
                                        <tbody>
                                            <tr>
                                                <td width="40%" class="clump">
                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;">
                                                        <tbody>
                                                            <tr>
                                                                <td width="35" height="25" valign="top"><img src="https://cdn.shopify.com/s/files/1/0065/7306/4236/files/email-phone-icon.png" alt="Phone" border="0" width="22" style="display:block; border:0; outline:none;" /></td>
                                                                <td width="" height="25" valign="top" align="left" style="font-family:'Poppins', sans-serif, Arial; font-size:12px; line-height:24px; font-weight:400; color:#2f3542;"> +91 9757486757</td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="4" style="padding:0 0 15px 10px;">
                                    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;">
                                        <tbody>
                                            <tr>
                                                <td width="60%" class="clump">
                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;">
                                                        <tbody>
                                                            <tr>
                                                                <td width="35" height="25" valign="top"><img src="https://cdn.shopify.com/s/files/1/0065/7306/4236/files/email-mail-icon.png" alt="Email" border="0" width="22" style="display:block; border:0; outline:none;" /></td>
                                                                <td width="" height="25" valign="top" align="left" style="font-family:'Poppins', sans-serif, Arial; font-size:12px; line-height:24px; font-weight:400; color:#2f3542;"><a href="mailto:data.analyst@flomattress.com" style="text-decoration:none; color:#2f3542;">data.analyst@flomattress.com</a></td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>

                            <tr>
                                <td colspan="4" style="padding:0 0 0 10px;">
                                    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;">
                                        <tbody>
                                            <tr>
                                                <td width="33%" class="clump">
                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;">
                                                        <tbody>
                                                            <tr>
                                                                <td width="35" height="25" valign="top"><img src="https://cdn.shopify.com/s/files/1/0065/7306/4236/files/email-internet-icon.png" alt="Web" border="0" width="22" style="display:block; border:0; outline:none;" /></td>
                                                                <td width="" height="30" valign="top" align="left" style="font-family:'Poppins', sans-serif, Arial; font-size:12px; line-height:24px; font-weight:400; color:#2f3542;"><a href="https://www.flomattress.com" style="text-decoration:none; color:#2f3542;">flomattress.com</a></td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>

                            <tr>
                                <td colspan="4" style="padding:10px 0 20px 0;">
                                    <a href="https://www.facebook.com/sleeponflo/" style="margin:0 5px; width: 25px;height: 25px;display: inline-block;vertical-align: middle;line-height: 25px;"><img src="https://cdn.shopify.com/s/files/1/0065/7306/4236/files/email-facebook-logo-icon.png" alt="Facebook" width="35" border="0" style="display:inline-block;border:0;outline:none;width: 20px;height: 20px;margin: 2.5px;" /></a>
                                    <a href="https://twitter.com/flomattressin" style="margin:0 5px; width: 25px;height: 25px;display: inline-block;vertical-align: middle;line-height: 25px;"><img src="https://cdn.shopify.com/s/files/1/0065/7306/4236/files/email-twitter-icon.png" alt="Twitter" width="35" border="0" style="display:inline-block;border:0;outline:none;width: 20px;height: 20px;margin: 2.5px;" /></a>
                                    <a href="https://www.linkedin.com/company/flo-mattress/?originalSubdomain=in" style="margin:0 5px; width: 25px;height: 25px;display: inline-block;vertical-align: middle;line-height: 25px;"><img src="https://cdn.shopify.com/s/files/1/0065/7306/4236/files/email-linkedin-icon.png" alt="LinkedIN" width="35" border="0" style="display:inline-block;border:0;outline:none;width: 20px;height: 20px;margin: 2.5px;" /></a>
                                    <a href="https://www.instagram.com/flomattress/?hl=en" style="margin:0 5px; width: 25px;height: 25px;display: inline-block;vertical-align: middle;line-height: 25px;"><img src="https://cdn.shopify.com/s/files/1/0065/7306/4236/files/email-instagram-icon.png" alt="Instagram" width="35" border="0" style="display:inline-block;border:0;outline:none;width: 20px;height: 20px;margin: 2.5px;" /></a>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="4">
                                    <p class="block-titel" style="font-size: 12px;line-height: 24px;font-weight: 400;color: #2f3542;">Featured In</p>
                                    <div class="autocenter">
                                        <img src="https://cdn.shopify.com/s/files/1/0065/7306/4236/files/email-brand-logo.png?v=1623778930" alt="Brand logo image" style="width: 150%; max-width: 100%; height: auto;" />
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="4" style="font-family:'Poppins', sans-serif, Arial; font-size:10px; line-height:18px; font-weight:400; color:#acb1bc; padding:10px 0 0 10px;">
                                    This message and any attachments are confidential and intended for the named addressee(s) only. If you have received this message
                                    in error, please notify immediately the sender, then delete the message. Any unauthorized modification, edition, use or
                                    dissemination is prohibited. The sender shall not be liable for this message if it has been modified, altered, falsified,
                                    infected by a virus or even edited or disseminated without authorization.
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
            </tr>
        </tbody>
    </table>
</body>
</html>"""

# ── Form fields ───────────────────────────────────────────────────────────────
first_name = st.text_input("First Name")
last_name  = st.text_input("Last Name")
phone      = st.text_input("Phone Number")
email      = st.text_input("Email ID")
job_title  = st.text_input("Job Title")

# ── Button ────────────────────────────────────────────────────────────────────
if st.button("Generate and open my email footer HTML file"):

    errors = []

    # --- Validate & clean First Name
    fn = first_name.strip()
    if not fn:
        errors.append("First Name cannot be empty.")
    elif len(fn.split()) > 2:
        errors.append("First Name should be one or two words only.")

    # --- Validate & clean Last Name
    ln = last_name.strip()
    if not ln:
        errors.append("Last Name cannot be empty.")
    elif len(ln.split()) > 2:
        errors.append("Last Name should be one or two words only.")

    # --- Validate Phone
    ph = phone.strip()
    if not ph:
        errors.append("Phone Number cannot be empty.")
    elif not re.fullmatch(r"\d{10}", ph):
        errors.append("Please enter a valid 10-digit phone number (digits only, no spaces or dashes).")

    # --- Validate Email
    em = email.strip()
    if not em:
        errors.append("Email ID cannot be empty.")
    elif not em.endswith("@flomattress.com"):
        errors.append("Please enter a valid Flo Mattress email address (must end with @flomattress.com).")

    # --- Validate Job Title
    jt = job_title.strip()
    if not jt:
        errors.append("Job Title cannot be empty.")

    # --- Show errors or generate
    if errors:
        for err in errors:
            st.error(err)
    else:
        full_name = f"{fn} {ln}"
        formatted_phone = f"{ph[:5]} {ph[5:]}"

        html_output = HTML_TEMPLATE
        html_output = html_output.replace("Tanmay Badgujar", full_name)
        html_output = html_output.replace("9757486757", formatted_phone)
        html_output = html_output.replace("data.analyst@flomattress.com", em)
        html_output = html_output.replace("Executive Data Analyst", jt)

        # Encode to base64 data URI and auto-open in new tab
        b64 = base64.b64encode(html_output.encode("utf-8")).decode("utf-8")
        data_uri = f"data:text/html;base64,{b64}"

        # JavaScript to open new tab automatically
        open_script = f"""
        <script>
            window.open("{data_uri}", "_blank");
        </script>
        """
        st.components.v1.html(open_script, height=0)

        st.success(f"✅ Footer generated for **{full_name}**! A new tab should have opened.")
        st.info(
            "**In the new tab:**\n\n"
            "1. Press **Ctrl + A** (Windows/Linux) or **Cmd + A** (Mac) to select everything.\n"
            "2. Press **Ctrl + C** / **Cmd + C** to copy.\n"
            "3. Open **Gmail → Settings (⚙️) → See all settings → General**.\n"
            "4. Scroll down to **Signature**, click into the signature box, and paste with **Ctrl + V** / **Cmd + V**.\n"
            "5. Scroll to the bottom and click **Save Changes**."
        )

        # Also offer a download as fallback
        st.download_button(
            label="⬇️ Download HTML file instead (if new tab didn't open)",
            data=html_output,
            file_name=f"{fn}_{ln}_Flo_Footer.html",
            mime="text/html"
        )
